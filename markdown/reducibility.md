---
title: Reducibility
...

# Reduction

In theoretic computation, we discuss the notion of "reducible".
A problem family $P_1$ is said to be **reducible** to another problem family $P_2$
if we know of some process that looks like

How to solve $p \in P_1$
:   1. convert $p$ into $q \in P_2$
    2. solve $q$
    3. convert the solution to $q$ into a solution of $p$

This concept will get much more attention in your Theory of Computation course,
including categorizing how much work the conversion can take;
but one example is useful in understanding logic.

One of the best-known introductory tests on computational theory defines reduction as follows:

> A _**reduction**_ is a way of converting one problem into another in such a way that a solution to the second problem can be used to solve the first problem.^[Michael Sipser, *Introduction to Computational Theory*. PWS Publishing (Boston, MA: 1997). ISBN: 0-534-94728-X]

# Logical reduction

Many proofs have the general form

1. Take the theorem and convert it into a different claim
2. Appeal to an already-existing proof of that different claim
3. Undo the conversion (or state that no undo is needed)

This is a logical reduction:
we *reduce* the new theorem to an old theorem.

The existence of reductions are often denoted using a subscripted $\le$ symbol:
$x \le_y z$ means "(new theorem) $x$ can be reduced to (old theorem) $z$, using only tools in $y$ to do the reduction."
There is no standard way to write "logically reducible"; we'll use $\le_{\mathrm logic}$ in this writeup.


## Proof by Induction

The inductive step in proof by induction is a very direct application of reduction:
we reduce $P(n+1)$ to $P(n)$, where $P$ is the inductive hypotheses^[Note: using $P$ (a predicate) as a symbol for the inductive hypotheses is something our textbook does often, but not something that is very common outside of that text.].
In other words, that case shows that $P(n+1) \le_{\mathrm{logic}} P(n)$.

Another way of thinking about proof by induction generally is that the inductive steps shows us, for any $n$, how to reduce $P(n)$ to $P(0)$: that is, $P(n) \le_{\mathrm{logic}} P(0)$.
This is shown by providing a way of constructing the proof for any given $n$.

{.example ...}
Consider the following proof of $\forall n \in \mathbb N \;.\; 0 = 2n \mod 2$.

:::proof
We proceed by induction.

**Base case**: When $n = 0$, $0 = 2n \mod 2$ because $2n = 0$.

**Inductive case**: Assume $2n = 0 \mod 2$. Then $2(n+1) = 2n+2$, and $2n + 2 = 2n \mod 2$.
But we know that $0 = 2n \mod 2$ our assumption, so $0 = 2(n+1) \mod 2$ as well.

By the principle of induction, it follows that $\forall n \in \mathbb N \;.\; 0 = 2n \mod 2$.
:::

If we consider this proof as a reduction template, we could prove $0 = 2(7) \mod 2$ as follows:

:::proof
$0 = 2(0) \mod 2$ because $2(0) = 0$.

$0 = 2(1) \mod 2$ because $2(1) = 2(0)+2$, and $2(0) + 2 = 2(0) \mod 2$.
But we know that $0 = 2(0) \mod 2$ by the previous step, so $0 = 2(1) \mod 2$ as well.

$0 = 2(2) \mod 2$ because $2(2) = 2(1)+2$, and $2(1) + 2 = 2(1) \mod 2$.
But we know that $0 = 2(1) \mod 2$ by the previous step, so $0 = 2(2) \mod 2$ as well.

$0 = 2(3) \mod 2$ because $2(3) = 2(2)+2$, and $2(2) + 2 = 2(2) \mod 2$.
But we know that $0 = 2(2) \mod 2$ by the previous step, so $0 = 2(3) \mod 2$ as well.

$0 = 2(4) \mod 2$ because $2(4) = 2(3)+2$, and $2(3) + 2 = 2(3) \mod 2$.
But we know that $0 = 2(3) \mod 2$ by the previous step, so $0 = 2(4) \mod 2$ as well.

$0 = 2(5) \mod 2$ because $2(5) = 2(4)+2$, and $2(4) + 2 = 2(4) \mod 2$.
But we know that $0 = 2(4) \mod 2$ by the previous step, so $0 = 2(5) \mod 2$ as well.

$0 = 2(6) \mod 2$ because $2(6) = 2(5)+2$, and $2(5) + 2 = 2(5) \mod 2$.
But we know that $0 = 2(5) \mod 2$ by the previous step, so $0 = 2(6) \mod 2$ as well.

$0 = 2(7) \mod 2$ because $2(7) = 2(6)+2$, and $2(6) + 2 = 2(6) \mod 2$.
But we know that $0 = 2(6) \mod 2$ by the previous step, so $0 = 2(7) \mod 2$ as well.
:::
{/}


## Proof by Contradiction

One way of viewing proof by contradiction is as a reduction to *modus tolens*: $\big((A \rightarrow B) \land (\lnot B)\big) \vdash (\lnot A)$.
Generally, the $B$ we use is $\bot$, which gives us the $\lnot B$ by defintion of $\lnot \bot$.
The reduction works as follows:

:::theorem
$\lnot A$
:::

:::proof
Because (*bulk of proof goes here*), $A \rightarrow \bot$.
(*we generally omit saying "But trivially, $\lnot \bot$"*)
By *modus tolens*, $\lnot A$.
:::

By far the most common way to prove $A \rightarrow B$ is to assume $A$ and prove $\vdash B$.
This uses the "conditional introduction" rule which can be formalized in TFL as

<table class="TFL">
    <tr><td>$i$</td><td>
        <table class="TFL">
            <tr><td>$i$</td><td>$A$</td></tr>
            <tr class="then"><td>$j$</td><td>$B$</td><td>&nbsp;</td></tr>
        </table>
    </td></tr>
    <tr class="then"><td>$k$</td><td>$A \rightarrow B$</td><td>$\rightarrow$I $i$</td></tr>
</table>

Thus, we could characterize proof by contradiction as

1. "Prove $A$" $\le_{\mathrm logic}$ "assume $\lnot A$, prove $\bot$" because
    2. "Prove $A$" $\le_{\mathrm logic}$ "prove $\lnot B$" via double negation, where $B = \lnot A$.
    3. "Prove $\lnot B$" $\le_{\mathrm logic}$ "prove $B \rightarrow \bot$" via modus tolens.
    4. "Prove $B \rightarrow \bot$" $\le_{\mathrm logic}$ "assume $B$, prove $\bot$" via conditional introduction.

However, since proof by contradiction is so common, we generally do not note these intermediate reductions,
treating the whole as a common type of proof.


## *reductio ad absurdum*

One of the oldest and best-known-outside-CS examples of reduction is the proof strategy *reductio ad absurdum* (ἡ εἰς τὸ ἀδύνατον ἀπόδειξις).
This is an informal version of proof by contradiction.
Basically it works by saying "*X* must be false because if it were true, *Y* would be true and it's clearly not."

{.example ...}
*I must not be the smartest person in the world; if I were, I'd be rich and famous.*

The above *reduces* being not being smartest to not being rich.
{/}

{.example ...}
*Time travel will never be discovered; if it were, some time traveler would have come back to now by now.*

The above *reduces* time travel existing to time travelers visiting the present.
{/}

As with all informal pseudo-proofs, *reductio ad absurdum* is susceptible to various fallacies.
One in particular is so common it has a special name: the [Slippery Slope fallacy](https://en.wikipedia.org/wiki/Slippery_slope).
Slippery slopes work by having a large number of steps ($A$ reduces to $B$ reduces to $C$ reduces to ... reduces to $Y$ reduces to $Z$)
and either hiding an invalid reduction in the middle somewhere where it might not be noticed
or by having each step being individually probable, but the combined probability being quite low.

