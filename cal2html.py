import re, markdown, dateutil, json
from datetime import timedelta, datetime

def yamlfile(f):
    from yaml import load
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader

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


def raw2cal(data, links=None):
    """Given the data from a cal.yaml, return a list of weeks,
    where each week is a list of seven data,
    where each day is either None or {"date":datetime.date, "events":[...]}
    """
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
            if (v['start'] > d or v['end'] < d) if type(v) is dict else v != d:
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
                    'title':data[ent['type']+'s'][ent['sidx']] or '',
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
                ent['sidx'] += 1
            # handle separate links file
            if links and d in links:
                for f in links[d].get('files',[]):
                    n = os.path.basename(f)
                    n = n[n.find('-')+1:]
                    ans[-1].setdefault('reading',[]).append({'txt':n,'lnk':f})
                if 'video' in links: ans[-1]['video'] = f['video']
                if 'audio' in links: ans[-1]['audio'] = f['audio']

        # handle assignments
        for task,ent in data['assignments'].items():
            if task[0] == '.': continue
            if 'due' not in ent: continue
            if ent['due'].date() != d: continue
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
    ans = ['<table id="schedule" class="calendar">']
    for week in cal:
        ans.append('<tr class="week">')
        for day in week:
            if day is not None:
                ans.append('<td class="day" date="{}">'.format(day['date'].strftime('%Y-%m-%d')))
                ans.append('<div class="wrapper">')
                ans.append('<span class="date w{1}">{0}</span>'.format(day['date'].strftime('%d %b').strip('0'), day['date'].strftime('%w')))
                ans.append('<div class="events">')
                for e in day['events']:
                    classes = [e[k] for k in ('section','kind','group') if k in e]
                    title = e.get('title','TBA')
                    more = []
                    if 'link' in e:
                        title = '<a target="_blank" href="{}">{}</a>'.format(e['link'], title)
                    for media in ('video', 'audio'):
                        if media in e:
                            more.append('<a target="_blank" href="{}">{}{}</a>'.format(
                                e[media],
                                media,
                                e[media][e[media].rfind('.'):]
                            ))
                    for reading in e.get('reading',[]):
                        if type(reading) is str:
                            more.append(reading)
                        else:
                            more.append('<a target="_blank" href="{}">{}</a>'.format(reading['lnk'], reading['txt']))
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
            else:
                ans.append('<td class="day" />')
        ans.append('</tr>')
    ans.append('</table>')
    external = '<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em"><path fill="#fff" stroke="#36c" d="M1.5 4.518h5.982V10.5H1.5z"/><path fill="#36c" d="M5.765 1H11v5.39L9.427 7.937l-1.31-1.31L5.393 9.35l-2.69-2.688 2.81-2.808L4.2 2.544z"/><path fill="#fff" d="M9.995 2.004l.022 4.885L8.2 5.07 5.32 7.95 4.09 6.723l2.882-2.88-1.85-1.852z"/></svg>'
    return re.sub(r'(<a[^>]*href="[^"]*//[^"]*"[^<]*)</a>', r'\1'+external+'</a>', ''.join(ans))
    return 


def cal2ical(cal, course, home, tz=None, sections=None, stamp=None):
    if tz is None: tz = 'America/New_York'
    now = datetime.utcnow().strftime('%Y%m%dT%H%M%S')
    
    ans = ['''BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//University of Virginia//{0}//EN
CALSCALE:GREGORIAN
NAME:{0}'''.format(course)]
    def icescape(s):
        s = s.replace('"', '').replace(':', '')
        s = s.replace('\\', '\\\\')
        s = s.replace('\n', '\\n')
        s = s.replace(r',', r'\,')
        s = s.replace(r',', r'\;')
        return s
    def fixlinks(l):
        for i in range(len(l)):
            l[i] = l[i].replace('<//','<https://')
            l[i] = re.sub(r'<([^><:]*)>', r'<{}\1>'.format(home.replace('\\','\\\\')), l[i])
    def encode(event):
        details = []
        if 'link' in event: details.append('see <' + event.get('link')+'>')
        if 'details' in event: details.append(event.get('details'))
        if 'reading' in event:
            for r in event['reading']:
                if type(r) is str: details.append(r)
                else: details.append('{txt} <{lnk}>'.format(**r))
        for media in ('video', 'audio'):
            if media in event:
                details.append('{}: <{}>'.format(media, event[media]))
        if 'day' in event:
            dts = ':{}'.format(event['day'].strftime('%Y%m%d'))
            dte = ':{}'.format((event['day'] + timedelta(1)).strftime('%Y%m%d'))
        elif 'from' in event and 'to' in event:
            dts = ';TZID={}:{}'.format(tz, event['from'].strftime('%Y%m%dT%H%M%S'))
            dte = ';TZID={}:{}'.format(tz, event['to'].strftime('%Y%m%dT%H%M%S'))
        else:
            raise Exception("Event without time: "+str(event))
        title = event.get('title','TBA')
        if 'section' in event: title = event['section']+' -- ' + title
        elif 'group' in event and event['group'] not in title:
            title = event['group']+' '+title
        fixlinks(details)
        return '''BEGIN:VEVENT
SUMMARY:{title}
DESCRIPTION:{notes}
DTSTART{dts}
DTEND{dte}
DTSTAMP:{now}Z
UID:{uid}@{course}.cs.virginia.edu
END:VEVENT'''.format(
            title=title, dts=dts, dte=dte, course=course, now=now,
            notes=icescape('\n'.join(details)),
            uid='{}-{}'.format(dts,title),
        )
    for week in cal:
        for day in week:
            if day:
                for event in day['events']:
                    if 'section' in event and sections and event['section'] not in sections: continue
                    ans.append(encode(event))
    ans.append('END:VCALENDAR\r\n')
    return '\r\n'.join(_.replace('\n','\r\n') for _ in ans)
    
if __name__ == '__main__':
    import os, os.path
    here = os.path.realpath(os.path.dirname(__file__))
    os.chdir(here)
    course = os.path.basename(here)


    import json, sys, yaml
    raw = yamlfile('cal.yaml')
    links = yamlfile('links.yaml') if os.path.exists('links.yaml') else {}
    cal = raw2cal(raw, links)
    with open('markdown/schedule.html', 'w') as fh:
        fh.write(cal2html(cal))

    with open('markdown/cal.ics', 'w') as fh:
        fh.write(cal2ical(cal, course, raw['meta']['home'], tz=raw['meta']['timezone']))
