import datetime, re, markdown, dateutil, json
# import pytz, unidecode

def yamlfile(f):
    from yaml import load
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader

    global default_tz
    if type(f) is str:
        with open(f) as stream:
            data = load(stream, Loader=Loader)
    else:
        data = load(f, Loader=Loader)
    return data


def dow(n):
    """string to int, with datetime's default 0=monday weekday numbering"""
    if type(n) is int: return n
    n = n.lower()
    if n.startswith('mo') or n == 'm': return 0
    if n.startswith('tu') or n == 't': return 1
    if n.startswith('we') or n == 'w': return 2
    if n.startswith('th') or n == 'h': return 3
    if n.startswith('fr') or n == 'f': return 4
    if n.startswith('sa') or n == 's': return 5
    if n.startswith('su') or n == 'u': return 6
    raise Exception("Unknown weekday: "+str(n))


def raw2cal(data):
    """Given the data from a cal.yaml, return a list of weeks,
    where each week is a list of seven data,
    where each day is either None or {"date":datetime.date, "events":[...]}
    """
    from datetime import timedelta, datetime
    s = data['Special Dates']['Courses begin']
    beg = s
    e = data['Special Dates']['Courses end']
    end = e
    while s.weekday() != 6: s -= timedelta(1)
    e = max(e, data['meta']['final']['start'].date())
    
    for sec, ent in data['sections'].items():
        ent['days'] = [dow(dows) for dows in ent['days']]
        ent.setdefault('sidx', 0)
    
    def onday(d):
        dt = datetime.fromordinal(d.toordinal())
        isexam = False
        ans = []
        
        # handle metadata
        if d == data['meta']['final']['start'].date():
            final = data['meta']['final']
            ans.append({
                "title":"Final Exam",
                "kind":"exam",
                "from":final['start'],
                "to":final['start'] + timedelta(0,60*final['duration']),
                "where":final['room']
            })
        for k,v in data['Special Dates'].items():
            if (v['start'] < d or v['end'] > d) if type(v) is dict else v != d:
                continue # does not apply
            if 'recess' in k or 'Reading' in k or 'break' in k:
                return ans # no classes
            if 'exam' in k.lower() or 'test' in k.lower() or 'midterm' in k.lower():
                isexam = True
            else:
                ans.append({
                    "title":k,
                    "kind":"special",
                    "day":d
                })
        if d < beg: return ans
        if d > end: return ans
        
        # handle sections
        for sec, ent in data['sections'].items():
            if d.weekday() not in ent['days']: continue
            if isexam and any((
                data['meta'].get('lecture exam') == (ent['type'] == 'lecture'),
                ent.get('exams')
            )):
                ans.append({
                    'section':sec,
                    'title':'Exam',
                    "kind":'exam',
                    "from":dt + timedelta(0,ent['start']),
                    "to":dt + timedelta(0,ent['start'] + 60*ent['duration']),
                    "where":ent['room']
                })
            elif ent['type']+'s' not in data or len(data[ent['type']+'s']) <= ent['sidx']:
                ans.append({
                    'section':sec,
                    'title':ent['type'],
                    "kind":ent['type'],
                    "from":dt + timedelta(0,ent['start']),
                    "to":dt + timedelta(0,ent['start'] + 60*ent['duration']),
                    "where":ent['room']
                })
            else:
                ans.append({
                    'section':sec,
                    'title':data[ent['type']+'s'][ent['sidx']],
                    "kind":ent['type'],
                    "from":dt + timedelta(0,ent['start']),
                    "to":dt + timedelta(0,ent['start'] + 60*ent['duration']),
                    "where":ent['room']
                })
                if ans[-1]['title'] in data['reading']:
                    tmp = data['reading'][ans[-1]['title']]
                    if type(tmp) is list:
                        ans[-1]['reading'] = tmp
                    else:
                        ans[-1]['reading'] = [tmp]
                # add from-lecture links
                ent['sidx'] += 1

        # handle assignments
        for task,ent in data['assignments'].items():
            if task[0] == '.': continue
            if 'due' not in ent: continue
            if ent['due'].date() != d: continue
            print(task, ent)
            group = ent.get('group', re.match('^[A-Za-z]*',task).group(0))
            tmp = data['assignments'].get('.groups',{}).get(group,{})
            tmp.update(ent)
            ent = tmp
            ans.append({
                'title':ent.get('title', task),
                'kind':'assignment',
                'group':group,
                'from':ent['due']-timedelta(0,900),
                'to':ent['due'],
            })
            if 'link' in ent: ans[-1]['link'] = ent['link']
            # add data for submission server
            
        return ans

    ans = []
    while s <= e:
        if s.weekday() == 6: ans.append([])
        events = onday(s)
        if len(events):
            ans[-1].append({'date':s,'events':events})
        else:
            ans[-1].append(None)
        s += timedelta(1)
    return ans

def cal2html(cal):
    ans = ['<table class="agenda">']
    for week in cal:
        ans.append('<tr class="week">')
        for day in week:
            ans.append('<td class="day">')
            if day is not None:
                ans.append('<div class="wrapper">')
                ans.append('<span class="date w{1}">{0}</span>'.format(day['date'].strftime('%d %b').strip('0'), day['date'].strftime('%w')))
                ans.append('<div class="events">')
                for e in day['events']:
                    classes = [e[k] for k in ('section','kind','group') if k in e]
                    title = e.get('title','TBA')
                    more = []
                    if 'link' in e:
                        title = '<a href="{}">{}</a>'.format(e['link'], title)
                    for media in ('video', 'audio'):
                        if media in e:
                            more.append('<a href="{}">{}{}</a>'.format(
                                e[media],
                                media,
                                e[media][e[media].rfind('.'):]
                            ))
                    for reading in e.get('reading',[]):
                        if type(reading) is str:
                            more.append(reading)
                        else:
                            more.append('<a href="{}">{}</a>'.format(reading['lnk'], reading['txt']))
                    if more:
                        ans.append('<details class="{}">'.format(' '.join(classes)))
                        ans.append('<summary>{}</summary>'.format(title))
                        ans.append(' <small>and</small> '.join(more))
                        ans.append('</details>')
                    else:
                        ans.append('<div class="{}">{}</div>'.format(' '.join(classes), title))
                ans.append('</div>')
                ans.append('</div>')
            ans.append('</td>')
        ans.append('</tr>')
    ans.append('</table>')
    return ''.join(ans)

    
if __name__ == '__main__':
    import json, sys, yaml
    raw = yamlfile('cal.yaml')
    cal = raw2cal(raw)
    with open('/tmp/tmp2.html', 'w') as fh:
        fh.write('''﻿<style>
table.calendar { 
    border-collapse: collapse; 
    width: 100%; 
    background: rgba(0,0,0,0.125); 
    border: 0.5ex solid rgba(0,0,0,0);
    border-radius: 1.5ex; 
}
table.calendar td:empty { padding: 0; height: 1.5em; }
table.calendar td { height: 100%; border: 0.25ex solid rgba(0,0,0,0); }
table.calendar span.date { 
    font-size: 70.7%;
    padding-left: 0.5ex;
    float:right;
    margin-top:-0.5ex;
}
table.calendar div.wrapper { 
    background: white;
    border-radius: 1ex;
    padding: .5ex;
    flex-direction:row;
    box-sizing:border-box; 
    width: 100%;
    height: 100%;
    overflow: hidden;
}
table.calendar div.wrapper div {
    padding: 0 0.5ex 0 0.5ex;
    margin: 0 -0.5ex 0 -0.5ex;
}
table.calendar div.wrapper div:first-child {
    padding-top: 0.5ex;
    margin-top: -0.5ex;
}
table.calendar div.wrapper div:last-child {
    padding-bottom: 0.5ex;
    margin-bottom: -0.5ex;
}


table.agenda { display: block; }
table.agenda tr {
    display: block; border-top: thick solid grey;
    min-height: 2em;
}
table.agenda td {
    display: table; border-top: thin dotted black; width: 100%;
    padding: 0;
}
table.agenda td:empty { display: none; }
table.agenda span.date.w0:before { content: "Sun "; }
table.agenda span.date.w1:before { content: "Mon "; }
table.agenda span.date.w2:before { content: "Tue "; }
table.agenda span.date.w3:before { content: "Wed "; }
table.agenda span.date.w4:before { content: "Thu "; }
table.agenda span.date.w5:before { content: "Fri "; }
table.agenda span.date.w6:before { content: "Sat "; }
table.agenda span.date {
    font-size: 70.7%; width:7em;
    vertical-align: middle; 
    display: table-cell;
}
table.agenda div.wrapper { display: table-row; }
table.agenda div.events { display: table-cell; vertical-align: middle; }

.assignment:before { content: "due: "; font-size: 70.7%; }
small { opacity: 0.5; }
.special, .exam { background: rgba(255,127,0,0.25); opacity: 0.75; }
span.date { font-family:monospace; }
details { padding-left: 1em; }
summary { margin-left: -1em; }

</style>''')
        fh.write(cal2html(cal))
