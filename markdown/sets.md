---
title: Sets
...

{.aside ...}
The first clause of §4 is "We have assumed that you’ve already been introduced to the concepts of sets...". The authors of that text may have assumed that, but I do not. This text is intended to fill in that gap.

Part of the reason this write-up exists is that sets are traditionally the domain of algebra, not discrete math; but the subset of algebra that is taught in secondary school and called "algebra" (as opposed to what is taught in university and called "algebra") often omits sets. Some of you had a broad algebra experience and already know sets, but many of you did not.
{/}

# Defining Sets

Let's build up a definition of set one step at a time.
I'll do this informally with an emphasis on ease of understanding
instead of formally with an emphasis on precision; if you want a precise definition instead, see §7.3.2.

1. **A set contains members.**
    
    **Set** is thus a term referring to a collection, kind of like a list in programming.
    **Member** is the mathematician's word for something inside a set;
    in programming, we more commonly call them *elements* instead.
    
    There is no constraint on the type of the members of set.

1. **We write a set with curly braces and commas.**
    
    For example, {1, 3} is a set. So is {dog, cat, mouse}.
    
    Arguably, {`x?y:z`, satisfaction, 2102, 🐉} is also a set, but sets whose members do not have some defined type are so uncommon some would say they are not actually sets.

1. **A member of a set has no other set-related properties besides membership in the set: not order or position in the set, not number of copies in the set, etc.**
    
    Thus, {1, 2} and {2, 1} are two ways of writing the same set.
    
    Also, {1, 2, 2} is nonsensical: {1, 2} already told us that the set had both 1 and 2 inside it; adding another 2 doesn't make any sense, any more than it makes sense to say "I'm a student and a logician and a logician." We might *guess* that they were being sloppy about sets and meant {1, 2}, but perhaps they made a typo and meant {1, 2, 3} instead? We simply can't tell.

1. **The only property of a set is its members.**
    
    Once you've written {1, 2}, you've written all there is to know about that set. This implies that we can talk about every {1, 2} as referring to the same set, even if we write it as {2, 1} or "the set containing 1 and 2" instead.
    
    Note that this observation is also true of numbers: once you've written 7, you've written all there is to know about it. We can talk about every 7 as referring to the same number, even if we write it as Ⅶ or "seven" instead.
    
    Note that we will define other properties which are derived from its members, such as *cardinality* (the number of members it has).

1. **A set can be empty. Both {} and $\emptyset$ represent the empty set.**
    
    Because a set's only property is its members, it is usual to speak of *the* empty set, not *an* empty set.

1. **A set can be infinite.**

    The set of integers is infinite. So is the set of even positive integers. So is the set of numbers which, when written in base 10, only contain the digit 2. So is the set of responses you could give to the question "how are you?". So is the set of examples I could add to this paragraph.

1. **A set can have sets as members.**
    
    {1} is a set; so is {{1}, {}, {84, 5}}; so is {1, {1, {}}, {{1}}, {{{2, {3}}}}}; so is the set of all two-element sets.
    
    Note that having sets inside other sets does not change any of the other rules.
    Thus {{1,2}, {2,1}} is nonsensical for the same reason {2, 2} is nonsensical: we wrote it as if it made sense to say the same value was a member of the set twice.

# Set operations and notation

## Membership

$m \in S$ is defined to mean "$m$ is a member of $S$"
:   Note that $m \in S$ is a predicate: $1 \in \{1,2,3\}$ is $\top$ and $1 \in \{2,4,6\}$ is $\bot$.
    
    A nuance of English I have observed, but have no formal definition to back up, is that while we usually speak of the *members* of a set, we usually read ∈ as "*element* of", not "*member* of". In most cases, if you use the wrong one of "member" or "element" people will understand you without difficulty.
    
    Set membership is ubiquitous in computing's use of sets.    

$m \notin S$ is defined to mean $\lnot(m \in S)$
:   You'll also rarely see ∋ and ∌, which mean the same thing as ∈ and ∉ but with the set on the left and the member on the right instead of the other way around.

Checking for membership in sets is a very common component of discrete mathematics as it is used by computer scientists.

## Sub- and super-sets

$A \subseteq B$ is defined to mean $\forall x. ((x \in A) \rightarrow (x \in B))$"
:   The $\subseteq$ symbol is pronounced "is a subset of".
    It intentionally looks somewhat like the symbol $\leq$
    because if $A \subseteq B$ then $A$ is "less than or equal to" $B$ in the sense that everything $A$ has, $B$ has too, and $B$ may have more.
    
        $\top$                 $\bot$
    --------------------    ---------------------
    {} ⊆ {1, 2}             {1, 2} ⊆ {2, 3}
    {1} ⊆ {1, 2}            {1, 2} ⊆ {1}
    {1, 2} ⊆ {1, 2}          
    {1, 2} ⊆ the integers   {1, 2.3} ⊆ the integers
    
    Subsets are very common in computing's use of sets.

$A \subset B$ is defined to mean $(A \subseteq B) \land (A \neq B)$
:   The $\subset$ symbol is pronounced "is a proper subset of".
    
        $\top$                 $\bot$
    --------------------    ---------------------
    {} ⊂ {1, 2}             {1} ⊂ {2, 3}
    {1} ⊂ {1, 2}            {1, 2} ⊂ {1}
                            {1, 2} ⊂ {1, 2}
    {1, 2} ⊂ the integers   {1, 2.3} ⊂ the integers

    Proper subsets are not very common in computing's use of sets.
    
    There exists an alternative vocabulary, where "⊂" is pronounced "subset" and "⊆" is pronounced "subset or equal". I have found that vocabulary to be uncommon and will not use it this semester.

$A \supseteq B$ means $B \subseteq A$; $A \supset B$ means $B \subset A$
:   The $\supseteq$ symbol is pronounced "is a superset of".
    The $\supset$ symbol is pronounced "is a proper superset of".

    Supersets are very common in computing's use of sets.

Checking for subsets is not used directly very often, but is often used to define other properties and putative theorems. One of the most famous unproven theorems of all, often phrased "**P** = **NP**"[^PNP], is not really interested in non-equality; what we hope to prove (or disprove) is **P** ⊂ **NP**, but so far the only proof we have is **P** ⊆ **NP**. The remaining piece of the proof is thus **P** ≠ **NP**.

[^PNP]:
    You'll learn more about this in CS 3102 or CS 4102, but a very brief summary may be helpful now.
    
    **P** and **NP** are two sets of *problems*, tasks we might want an algorithm to solve, defined by some characteristics of the most efficient algorithm that could exist to solve that problem. Glossing over a lot of important details,
    
    P
    :   The problems that can be solved efficiently enough to be worth trying
    
    NP
    :   The problems for which a putative answer can be checked to see if they are actually answers efficiently enough to be worth trying
    
    There's some beautiful reasoning in computational theory that has shown a large set of problems in **NP** (the "**NP** complete problems") such that, if any one of them is in **P**, so is the entirety of the set **NP**. So if someone could just solve one of those problems efficiently, all of those other problems we wish we could solve but can't will suddenly all become solvable too! A huge boon for computation, leading to people wanting to show **P** = **NP**.
    
    However, one particular problem makes us hope the truth is **P** ≠ **NP** instead: public-key encryption. I want my computer to be able to solve puzzles that no other computer can solve, but all other computers can check to see if I solved correctly, so that my solving a puzzles from that set can prove to other computers that I'm me and not someone else. That (with some other number-theoretic magic) lets me communicate to servers with confidence that it's just the two of us talking and no one else is pretending to be them or listening in. In other words, I rely on solving the puzzle being in **NP** but not **P** for everyone that does not have some secret only I have. But if someone proves that **P** = **NP** then having my secret is no longer necessary: everyone will be able to solve all the puzzles they can check the answer to, and much of modern computer security will collapse.
    
    Arguably, all of digital commerce is gambling on **P** ≠ **NP** being true, despite no proof of that existing. This may be the largest bet ever placed in the history of the world.

## Sets from other sets

$A \cup B$ is defined to mean "a set $S$ such that $\forall x. (x \in S \leftrightarrow ((x \in A) \lor (x \in B)))$"
:   The $\cup$ symbol is pronounced "union", and $A \cup B$ is called "the union of $A$ and $B$".
    It intentionally looks similar to $\lor$ to suggest a value is a member of the union of $A$ and $B$ if it is a member of $A$ *or* a member of $B$.
    
    Note that $(A \subseteq B) \leftrightarrow ((A \cup B) = B)$.
    
        $A$                     $B$                 $A \cup B$
    ----------------        ----------------    -------------------------------
    {1, 2}                  {1, 2}              {1, 2}
    {1, 2}                  {}                  {1, 2}
    {1, 2}                  {5, 6}              {1, 2, 5, 6}
    {1, 2, 4, 8}            {2, 4, 6, 8}        {1, 2, 4, 6, 8}
    the positive numbers    {0}                 the non-negative numbers
    the even integers       the odd integers    the integers
    UVA students            UVA employees       UVA denizens

    Union is common in computing's use of sets.

$A \cap B$ is defined to mean "a set $S$ such that $\forall x. (x \in S \leftrightarrow ((x \in A) \land (x \in B)))$"
:   The $\cap$ symbol is pronounced "intersection", and $A \cap B$ is called "the intersection of $A$ and $B$".
    It intentionally looks similar to $\land$ to suggest a value is a member of the intersection of $A$ and $B$ if it is a member of $A$ *and* a member of $B$.
    
    Note that $(A \subseteq B) \leftrightarrow ((A \cap B) = A)$.
    
        $A$                     $B$                 $A \cap B$
    ----------------        ----------------    -------------------------------
    {1, 2}                  {1, 2}              {1, 2}
    {1, 2}                  {}                  {}
    {1, 2}                  {5, 6}              {}
    {1, 2, 4, 8}            {2, 4, 6, 8}        {2, 4, 8}
    the positive numbers    the integers        the positive integers
    beach paraphernalia     towels              beach towels
    
    If $A \cap B = {}$, we say that $A$ and $B$ are **disjoint**.
    Less commonly, **overlap** is used to mean "are not disjoint".

    Intersection is common in computing's use of sets.

$A \setminus B$ is defined to mean "a set $S$ such that $\forall x. (x \in S \leftrightarrow ((x \in A) \land (x \notin B)))$"
:   The $\setminus$ symbol is pronounced either "minus" or "set minus".
    $A \setminus B$ has everything that $A$ has provided $B$ does not have it.
    It is rarely used in computing, but does show up from time to time.
    I have no idea how they picked a symbol that looks like backwards division.

    Note that $(A \subseteq B) \leftrightarrow ((A \setminus B) = \emptyset)$.
    
        $A$                 $B$                     $A \setminus B$
    ----------------    ----------------        -------------------------------
    {1, 2}              {1, 2}                  {}
    {1, 2}              {}                      {1, 2}
    {1, 2}              {5, 6}                  {1, 2}
    {1, 2, 4, 8}        {2, 4, 6, 8}            {1}
    the integers        the positive numbers    the negative integers
    UVA denizens        UVA students            UVA employees 
    
    Set minus is relatively uncommon in computing's use of sets.

pow$(A)$ or $\mathcal{P}(A)$ is defined to mean "a set $S$ such that $\forall x. (x \in S \leftrightarrow (x \subseteq A))$" 
:   pow$(A)$ or $\mathcal{P}(A)$ (the two are used interchangeably, though any given text will use only one of the two) is called "the power set of $A$" and is the set of all subsets of $A$.
    
    Note that every set (even {}) has at least one subset: {}; thus a power set is *never* empty, $\emptyset \in \mathcal{P}(A)$ is a tautology, and $\emptyset = \mathcal{P}(A)$ is a contradiction regardless of what set $A$ is.

        $A$     $\mathcal{P}(B)$
    ----------- --------------------------------------------------------------
    {}          {{}}
    {1}         {{}, {1}}
    {1, 2}      {{}, {1}, {2}, {1, 2}}
    {1, 2, 3}   {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
    {{1, 2}, 3} {{}, {{1, 2}}, {3}, {{1, 2}, 3}}
    {{}}        {{}, {{}}}
    
    Power sets are uncommon in computing's use of sets.

Note that there is no set-notation syntax for common programming tasks like adding an element to a set or removing it from a set, nor is there a union-parallel for $\oplus$. If you need to approximate these actions, use 

Concept             Set notation                        actually
----------------    --------------------------          ---------------------
"add" $x$ to $S$    $S \cup {x}$                        a set like $S$ except it also has $x$ in it
"remove" $x$ to $S$ $S \setminus {x}$                   a set like $S$ except it does not have $x$ in it
$A$ "xor" $B$       $(A \cup B) \setminus (A \cap B)$   a set with elements in $A$ or $B$ but not both

## Counting Members

$|A|$ means "the number of distinct values that are members of $A$
:   We call this notion **cardinality**
    and read $|A|$ as "the cardinality of $A$".
    
    Cardinality is related to, but distinct from, the idea of the length of a list: the list `[3, 1, 4, 1]` has length 4 but only 3 distinct elements, so the set of its elements is {1, 3, 4} and has cardinality 3.
    
    Cardinality is always either a natural number (that is, a non-negative integer) or infinite.
    There are actually more than one kind of infinite that cardinality can be, but we won't get into that in this writeup.
    
        $A$                             $|A|$
    -----------------------------   ------------
    {}                              0
    {1, 2}                          2
    {{1, 2}}                        1
    {1, {2, 3}}                     2
    the two-digit numbers           90
    the integers                    $\infty$
    $\mathcal{P}$({1, 3, 5, 7})     16
    $\mathcal{P}(A)$                $2^{|A|}$
    
    
    Cardinality is commonly used in theoretical computer science, but rare elsewhere in computing.

## Set-builder notation

See §4.1.4. We'll use this a lot.

{.aside ...}
Python (alone among the languages I use regularly) has a variation of set-builder notation. For example, the set-builder notation $\{x \in \mathbb{Z} \;|\; x^3-30x+1>0\}$ would be written `{x for x in Z if x**3-30*x+1 > 0}`{.python}, though you'd have to define a sensible, finite `Z` first (perhaps `range(-10,11)`{.python}).
It also allows computation after the selection, such as `[x**3 for x in range(15) if (x**0.5)%1 == 0]`{.python} as a list of cubes of perfect squares less than 15.
{/}

## Common sets

There are some sets that are so common they have their own special symbol.
§4.1.1 has a reasonable list of these.

Note that even in handwriting, you have to double at least one of the mostly-vertical lines for people to know you mean the set; "Z" is not the set of integers, "ℤ" is.
The official word for this orthography is "double-struck" as in "ℝ is a double-struck R," but you can probably make it through your entire life in computing (including this class) without ever needing to know that word.

# Quantifiers and Sets

Quantifiers are often used with sets. Set-notation quantifiers and domain-bound quantifiers can each be defined in terms of the other.
Note that one of our textbooks uses only domain-bound quantifiers and the other only set-notation quantifiers.

## Core notation

The notation "$\forall x \in S \;.\; P(x)$" means "The predicate $P(x)$ is true for every $x$ in the set $S$". It does not say anything about the truth or falsehood of $P(x)$ for $x$ not in $S$, nor does it assert that there are any members of $S$.

The notation "$\exists x \in S \;.\; P(x)$" means "There is at least one element of $S$, and at least one element of $S$ makes the predicate $P(x)$ true". It does not say anything about the truth or falsehood of $P(x)$ for $x$ not in $S$, nor if there are more (or even all) members of $S$ that also make $P(x)$ true.

The notation "$\forall x,y \in S$" is shorthand for "$\forall x \in S \;.\; \forall y \in S$".

The notation "$\exists x,y \in S$" is shorthand for "$\exists x \in S \;.\; \exists y \in S$".

## Converting "$\forall x \in S\;.\; \cdots$" to "$\forall x\;.\; \cdots$"

Re-write "$\forall x \in S \;.\; \cdots$" as "$\forall x \;.\; x \in S \rightarrow \cdots$".

If a domain is not specified and all quantifiers are given with sets, the implicit domain is union of all such sets or any superset containing that union.

## Converting "$\forall x\;.\; \cdots$" to "$\forall x \in S\;.\; \cdots$"

Define a set $U$ representing the entire domain. The symbol $U$ is not required, but is often used with the intent that it suggest the "universal set" or the "universe of discourse". In handwriting, $U$ and $\cup$ are easily confused so a different letter should be used instead.

Replace all "$\forall x \;.\; \cdots$" with "$\forall x \in U \;.\; \cdots$"



