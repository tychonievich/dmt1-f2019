---
title: Open Sets
...

This document has several goals.
First, it discusses a few ideas you should probably be familiar with,
including limitations on well-ordering and inductive proofs.
Second, it provides several examples of proof by contradiction.
Third, it gives an opportunity to discuss several proof style topics
such as levels of detail, how to present multiple poofs of similar structure, and the somewhat controversial phrase "*mutatis mutandis*".

# Lack of largest and smallest values

:::theorem
There is no smallest rational number larger than 0.
That is, $$\forall n_1 \in \mathbb Q^{+} \;.\; \exists n_2 \in \mathbb Q^{+} \;.\; n_2 < n_1$$
:::

:::proof
We proceed by contradiction.

Assume
$$\lnot\Big( \forall n_1 \in \mathbb Q^{+} \;.\; \exists n_2 \in \mathbb Q^{+} \;.\; n_2 < n_1 \Big)$$
Applying equivalence rules, that is the same as assuming
$$\exists n_1 \in \mathbb Q^{+} \;.\; \nexists n_2 \in \mathbb Q^{+} \;.\; n_2 < n_1$$
Let $n$ be one such $n_1$.
Consider $m = \frac{n}{2}$.
Because $n \in \mathbb Q^{+}$, $n$ is positive; because $2 > 1$, we have $0 < m < n$.
Because $n \in \mathbb Q^{+}$, $n$ is rational, and the division of two rational numbers is rational, so $m$ must be rational, and because $0 < m$ we have $m \in \mathbb Q^{+}$.
But that contradicts our assumption that $\nexists n_2 \in \mathbb Q^{+} \;.\; n_2 < n$.

Because our assumption led to a contradiction, our assumption must be false; that is,
$$\forall n_1 \in \mathbb Q^{+} \;.\; \exists n_2 \in \mathbb Q^{+} \;.\; n_2 < n_1$$
must be true.
:::

Using this theorem, we can prove two related more general corollaries:

:::corollary
For any rational number, there is no smallest rational number larger than it.
That is, 
$$
\forall q, n_1 \in \mathbb Q \;.\; n_1 > q \rightarrow \exists n_2 \in \mathbb Q \;.\; q < n_2 < n_1$$
:::

:::proof
We proceed by contradiction.

Suppose there was some $q$ for which corollary 1 was false.
Let $q_0$ be the smallest element of $\mathbb Q$ larger than $q$.
Then $q_0-q$ must be the smallest elements of $\mathbb Q^{+}$.
But we know from theorem 1 that there is no smallest element of $\mathbb Q^{+}$.
Thus, our supposition must be false, meaning corollary 1 must be true.
:::

{.aside ...}
Note the far less formal approach of the proof of corollary 1
compared to the proof of theorem 1.
There is no one right level of formality for proofs,
but often if one proof largely looks like another we try to present it more briefly than the first,
assuming the reader can use the formality of the first as a template for expanding the second if they are so inclined.

Of course, sometimes we are wrong about how comfortable the reader will be with brevity.
But if we wrote it out in full sometimes we'd be wrong about how happy they'd be with that full detail too.
Guessing the mind of the reader if part of the risk associated with any creative language art, even very specialized ones like proof writing.

We use an even briefer approach in the next proof.
{/}

:::corollary
For any rational number, there is no largest rational number smaller than it.
That is, 
$$
\forall q, n_1 \in \mathbb Q \;.\; n_1 < q \rightarrow \exists n_2 \in \mathbb Q \;.\; n_1 < n_2 < q$$
:::

:::proof
We proceed by contradiction.

Suppose there was some $q$ and $n_1$ for which corollary 2 was false.
Then $-q$ and $-n_1$ would make corollary 1 false,
which it is not.
Thus, there are no such $q$ and $n_1$, meaning corollary 2 is true.
:::

The above proofs also work for any other numbers that are closed under division by 2. In particular,

:::theorem
There is no smallest real number larger than $x$
nor a largest real number smaller than $r$ for any $r \in \mathbb R$
:::

The proofs of Theorem 1 and Corollaries 1 and 2 apply, *mutatis mutandis*, to Theorem 2 as well.

{.aside ...}
The Latin phrase "*mutatis mutandis*" means "with the necessary changes" and is used in formal writing to mean "copy-paste is not enough, but we know you can figure out the small changes that are needed so we're not going to waste your time listing them." In this case, the changes are replacing all $\mathbb Q$ with $\mathbb R$ and all references to "rational" with "real".

Some authors feel that saying *mutatis mutandis* is inappropriate: either you should trust the reader to know that there are trivial changes needed without saying so, or the changes were not trivial enough to elide in this way. I was trained by logicians who felt that adding it added clarity, indicating that some changes are needed. You are welcome to pick your own feelings on this point.
{/}

# Open Sets

:::definition
A non-empty set is said to be **open** if its members are ordered but it has no largest or smallest element.
:::

:::theorem
For any $q_1, q_2 \in \mathbb Q \;.\; q_1 < q_2$,
the set defined as $\big\{ q \;\big|\; q \in \mathbb Q \land q_1 < q < q_2 \}$
is an open set.
:::

:::proof
Let $A(q_1, q_2) = \big\{ q \;\big|\; q \in \mathbb Q \land q_1 < q < q_2 \}$
The smallest element of $A(q_1,q_2)$ would then be the smallest rational number larger than $q_1$ which, per corollary 1, does not exist, so $A(q_1,q_2)$ has no smallest element.
By a similar logic and corollary 2, $A(q_1,q_2)$ also has no largest element.
Thus, it is an open set.
:::

Some authors refer to sets with a largest but not smallest element (or a smallest but not largest) as "half-open," while others call such sets simply "open."

A set that is not open is called **closed**, but that term is a bit nuanced in use.
Some sets are unambiguously closed, like $\{x \;|\; x \in \mathbb R \land -1\leq x\leq 1\}$,
but others have open-like gaps inside them, like $\{x \;|\; x \in \mathbb R \land -1\leq x < 1 \lor 2 < x \leq 3\}$.
How to handle such sets, and if they ought to be called closed or not, is beyond the scope of this course.

Because open sets exist, proofs that rely on a smallest element of a set,
such as the well ordering principle and many inductive proofs,
need to first verify that the set they are handling has such a smallest element.
