---
title: Add-ons to MCS
license: <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png" /> CC-BY-SA 3.0</a> license</a>.
...

# Sets

See the separate [sets writeup](sets.html) and [sets practice](set-practice.html).

# Sequences

> The following includes all of the text from MCS 4.2 with some clarifications and some additional definitions that MCS assumes without defining.

Sets provide one way to group a collection of objects. Another way is in a **sequence**, which is a list of objects called **terms** or **components**. Short sequences are commonly described by listing the elements between parentheses; for example, $(a, b, c)$ is a sequence with three terms.

While both sets and sequences perform a gathering role, there are several differences.

- The elements of a set are required to be distinct, but terms in a sequence can be the same. Thus, $(a, b, a)$ is a valid sequence of length three, but $\{a, b, a\}$ is an incorrect way of writing a set, and if taken as a set is most likely a set with two elements, not three.

- The terms in a sequence have a specified order, but the elements of a set do not. For example, $(a, b, c)$ and $(a, c, b)$ are different sequences, but $\{a, b, c\}$ and $\{a, c, b\}$ are the same set.

- Texts differ on notation for the empty sequence; we use $\lambda$ for the empty
sequence; others use $\epsilon$, $\varepsilon$, or $()$.

Length two sequences are called **pairs**^[Some texts call them **ordered pairs**.].
Length one sequences are commonly treated as being identical to their single term, with no special action needed to convert between a length-one sequence and a non-sequence value.

The product operation is one link between sets and sequences. A **Cartesian product** of sets, $S_1 \times S_2 \times \cdots \times S_n$, is a new set consisting of all sequences where the first component is drawn from $S_1$, the second from $S_2$, and so forth. For example, $\mathbb N \times \{a,b\}$ is the set of all pairs whose first element is a nonnegative integer and whose second element is an $a$ or a $b$:

$$\mathbb N \times \{a,b\} = \{(0,a), (0,b), (1,a), (1,b), (2,a), (2,b), \dots\}$$

A product of $n$ copies of a set $S$ is denoted $S^n$. For example, $\{0,1\}^3$ is the set of all 3-bit sequences:

$$\{0,1\}^3 = \{(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)\}$$

The special notation $S^{*}$ means the set $\big\{x \;\big\|\; \exists n \in \mathbb N \;.\; x \in S^n \big\}$. The superscript asterisk is called a **Kleene star**.

$$\{0,1\}^{*} = \{\lambda, (0), (1), (0,0), (0,1), (1,0), (1,1), (0,0,0), (0,0,1), \dots\}$$


A **symbol** is a mathematical entity whose only meaning is its identity. Symbols are often written in a fixed-width font or as code; for example, 1 is a number and `1` is the symbol used to represent that number.
A sequence of symbols is called a **string** and is often written without the parentheses and commas, sometimes between quotes and other times not. For example, the following all refer to the same string: (`1`, `1`, `0`), `110`, "`110`".

# Functions

In addition to the material in MCS, the following is worth noting:

## Addenda to 4.3.1

MCS defines functions as having a set as their domain, but then provides examples of multiple-argument functions. There are two common ways to handle multiple-argument functions:

A domain of sequences
:   If $f(x,y)$ is defined for $x \in X$ and $y \in Y$, resulting in elements of $Z$, then we say $f : (X \times Y) \rightarrow Z$; and so on for longer argument lists.
    
    Thus, 4.3.1's function's types are
    
    $$f_1 : \mathbb R \rightarrow \mathbb R$$

    $$f_2 : \mathbb (\{0,1\}^{*} \times \{0,1\}^{*}) \rightarrow \{0,1\}^{*}$$
    
    $$f_3 : \mathbb (X \times \mathbb N) \rightarrow X^{*}$$

    $$f_4 : \mathbb (\{\top,\bot\} \times \{\top,\bot\}) \rightarrow \{\top,\bot\}$$

    $$f_5 : \mathbb \{0,1\}^{*} \rightarrow \mathbb N$$
    
    (note: the domain of $x$ in $f_3$ is undefined in MCS).

A function that yields a function
:   <!-- check: is this the Curry-Howard Isomorphism? -->
    A different way to handle multiple arguments is to evaluate them one at a time, with each partial evaluation resulting in a function with one fewer argument. Thus, if $f(x,y)$ is defined for $x \in X$ and $y \in Y$, resulting in elements of $Z$, then we say $f : X \rightarrow (Y \rightarrow Z)$ or (because the function-type arrow $\rightarrow$ is right-associative) simply $f : X \rightarrow Y \rightarrow Z$; and so on for longer argument lists.
    
    For example, consider the function $f(x,y,z) = x + y - z$. We could then say that $f(3)$ is a new function defined by the formula $3 + y - z$.
    $f(3,4)$ is shirt-hand for f(3)(4)$: that is, we evaluate $f(3)$ to get a function which we evaluate at $y=4$ to get $7 - z$.
    
    This seemingly convoluted representation is common in programming language research and present in the type system of some functional programming languages.
    
    Thus, 4.3.1's function's types are
    
    $$f_1 : \mathbb R \rightarrow \mathbb R$$

    $$f_2 : \mathbb \{0,1\}^{*} \rightarrow \{0,1\}^{*} \rightarrow \{0,1\}^{*}$$
    
    $$f_3 : X \rightarrow \mathbb N \rightarrow X^{*}$$

    $$f_4 : \mathbb \{\top,\bot\} \rightarrow \{\top,\bot\} \rightarrow \{\top,\bot\}$$

    $$f_5 : \mathbb \{0,1\}^{*} \rightarrow \mathbb N$$
    
    (note: the domain of $x$ in $f_3$ is undefined in MCS).
    
   
Every function can be written as a (possibly infinite) set of pairs, where the first term of each pair is an element of the domain and the second term of each pair is an element of the codomain. For example, $f_4$ can be written as $\Big\{
\big((\bot,\bot), \top\big),
\big((\bot,\top), \top\big),
\big((\top,\bot), \bot\big),
\big((\top,\top), \top\big)
\Big\}$.

## Addenda to 4.3.2

For every set $S$ there is a special function $f : S \rightarrow S$ defined as $f(x) = x$ and called **the identity function** (the definite article "the" is a bit misleading, as there is one such identity function for each possible set). There is no single standard notation for the identity function.

If, for two functions $f$ and $g$, both $f \circ g$ and $g \circ f$ are both identity functions, then we call $f$ and $g$ one another's **inverses**.
We often write the inverse of a function $f$ as $f^{-1}$.
Not all functions have inverses; those that do are called "invertible."

# Binary Relations

MCS 4.4 is a bit confusing when it comes to the relationship between functions and relations. Here's another take:

- Relations answer "yes/no" questions: "is 3 less than 2?", "does Tychonievich love programming?" etc.
- Functions answer "what is" questions: "what is the cube root of 2?", "what is Tychonievich's favorite poem?"
- Every function can be re-posed as a relation by guessing: "is the cube root of 2 1.4562?", "is Tychonievich's favorite poem *The Panther* by Ogden Nash?"
- A relation can only be re-posed as a function if there is a unique answer; "what is 3 less than?" and "what does Tychonievich love?" don't have single answers.
- If a relation can be re-posed as a function, we sometimes say the relation is a function.

The names of most of the various properties of relations show up quite rarely and, when they do, you can generally look them up; but the underlying questions are worth understanding:

In the,  are there values related to    if so we call it    if not we call it
-------- ---------------                ------------------  ------------------------
domain   nothing?                       partial             total
domain   multiple things?               non-functional      functional
codomain nothing?                       non-surjective      onto or surjective
codomain multiple things?               non-injective       one-to-one or injective

"Partial" and "total" are usually only discussed in relation to functions.
A total functional sujective injective relation is the same as a bijection, and is an invertable function.

The subset of these properties that apply to functions show up often enough that we'll want you to memorize them: **total** vs **partial** are moderately important, and **invertible** is very important.
