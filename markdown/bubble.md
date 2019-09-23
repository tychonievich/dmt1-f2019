---
title: A Proof about Bubble-Sort
...

# Preliminaries

There are many sorting algorithms, some better than others.
There exist strictly better algorithms than bubble sort
(i.e., faster, lower-power, same-space, and simpler),
there very inefficiency of bubble sorts makes a proof of its correctness interesting.

# Algorithm

:::definition
Let an element in a list be considered **out of order** if it is followed in the list by another value strictly smaller than itself.

An element that is not *out of order* is said to be **in order**.
:::

Observe that by this definition, the last element in the list cannot be out of order, but theoretically all other elements can.
That theory can be realized in practice by a list of unique elements sorted in descending order, with the first element being the largest and the last the smallest.


Consider the following algorithm:

Given
:   A list $x$ with $n$ elements, $x_1$ through $x_n$

Do
:   1. **repeat** the following **until** $x$ contains no out-of-order elements
    2.     **for each** $i$ from $1$ to $n-1$
    3.         **if** $x_i$ is *out of order* **then**
    4.             swap $x_i$ and $x_{i+1}$
    5.        **end if**
    6.     **end for**
    7. **end repeat**

# Proof of Correctness


:::theorem
Given any finite list $x$, the above algorithm will terminate after no more than $n-1$ iterations of the outer loop.
:::

To prove this theorem, we first define a *fixed tail* of a list and then prove a lemma about the inner loop.

:::definition
A **fixed tail** of a list is a (possibly empty) suffix of the list such that both (a) no element outside the tail is larger than any element inside the tail and (b) all elements in the tail are *in order*.

The **maximal fixed tail** of a list is the largest suffix of the list that is a *fixed tail*.
The portion of a list that is not part of it's *maximal fixed tail* is the **body** of the list.
:::

:::lemma
Each run of the inner loop of the algorithm (lines 2--6) increases the length of the list's *maximal fixed tail* by at least one.
:::

:::proof
Consider the largest element of the *body* of the list (if there are several elements of that value, consider the one with the largest index).
Because no element before it is larger than it, the condition on line 3 will keep line 4 from moving it to an earlier index.
Because it is larger than every element in the body after it, line 4 will keep pushing it to the next position until it reaches the end of the body.
Because every element of the original *maximal fixed tail* is at least as large as any element of the *body*, the element will then be *in order* and stop moving.
Because a *fixed tail* is *in order*, none of its elements will move either.
Because the new element has no elements outside the tail that is larger than it, and it is in order, it becomes part of a new, larger, *maximal fixed tail*.
:::

With this lemma, we can now prove the original theorem

:::proof
The list $x$ initially has a *maximal fixed tail* of at least 0 elements.
After each iteration of the outer loop, the *maximal fixed tail* increases in length by at least 1 element; thus, after $n-1$ iterations the *maximal fixed tail* must include all but the first element of the list.
By definition, all elements in the *fixed tail* are *in order*, so it remains to show only that the first element of the list is also *in order*.
Because the element following the first element is in a *fixed tail*,
the element following the first element cannot be smaller than the first element.
Hence, the first element is also *in order*
and the outer loop will terminate.
:::

