---
title: De Morgan's Law
...

:::theorem
For any expressions $P$ and $Q$, the expression $\lnot(P \land Q)$ is equivalent to the expression $(\lnot P) \lor (\lnot Q)$
:::

This is one of two "De Morgan's laws", named after Augustus De Morgan who died in 1871; however, its use and expression is roughly as old as formal logic itself.

# Truth Table: brute-force all cases

A truth table that shows the two expressions are equivalent
is an exhaustive analysis, the most tedious kind of proof by cases.
We might thus categorize it as a form of whiteboard proof,
though it is often treated as its own special thing.

 $P$   $Q$  |  $\lnot$   $(P \land Q)$  |  $(\lnot P)$   $\lor$    $(\lnot Q)$
----- ----- - --------- --------------- - ------------- --------- -------------
false false | **true**      false       |   true        **true**    true
false true  | **true**      false       |   true        **true**    false
true  false | **true**      false       |   false       **true**    true
true  true  | **false**     true        |   false       **false**   false

# Proof by Cases: prose

:::proof
Let **N** represent the expression $\lnot(P \land Q)$ and **O** represent the expression $(\lnot P) \lor (\lnot Q)$.

The proof is by case analysis.
There are two cases: either $P$ is true or it is false.

Case 1: $P$ is true
:   **N** is $\lnot (\top \land Q)$; using the identity of AND, this can be re-written as $\lnot Q$.
    **O** is $(\lnot \top) \lor (\lnot Q)$, which is equivalent to $\bot \lor (\lnot Q)$; using the identity of OR, this can be re-written as $\lnot Q$.
    Because **N** and **O** are equivalent to the same thing, they are equivalent to each other. Thus the theorem holds in this case.

Case 2: $P$ is false
:   **N** is $\lnot (\bot \land Q)$; using the zero of AND, this can be re-written as $\lnot \bot$, which is $\top$.
    **O** is $(\lnot \bot) \lor (\lnot Q)$, which is equivalent to $\top \lor (\lnot Q)$; using the zero of OR, this can be re-written as $\top$.
    Because **N** and **O** are equivalent to the same thing, they are equivalent to each other. Thus the theorem holds in this case.

Because the theorem holds in all cases, it is true.
:::

# Proof by cases: TFL

In small step logics, such as machine-checkable proofs,
a proof by cases works by introducing a sub-proof for each case.

<table class="TFL">
    <tr><td>1</td><td>$\lnot(P \land Q)$</td></tr>
    <tr class="then"><td>2</td><td>
        <table class="TFL">
            <tr><td>2</td><td>$P$</td></tr>
            <tr class="then"><td>3</td><td>
                <table class="TFL">
                    <tr><td>3</td><td>$Q$</td></tr>
                    <tr class="then"><td>4</td><td>$P \land Q$</td><td>$\land$I 2, 3</td></tr>
                    <tr><td>5</td><td>$\perp$</td><td>$\lnot$E 1, 4</td></tr>
                </table>
            </td></tr>
            <tr><td>4</td><td>$\lnot Q$</td><td>$\lnot$I 3</td></tr>
            <tr><td>5</td><td>$\lnot P \lor \lnot Q$</td><td>$\lor$I 4</td></tr>
        </table>
    </td></tr>
    <tr><td>3</td><td>
        <table class="TFL">
            <tr><td>3</td><td>$\lnot P$</td></tr>
            <tr class="then"><td>4</td><td>$\lnot P \lor \lnot Q$</td><td>$\lor$I 3</td></tr>
        </table>
    </td></tr>
    <tr><td>4</td><td>$\lnot P \lor \lnot Q$</td><td>LEM 2, 3</td></tr>
</table>

TFL proofs by cases help demonstrate two important principles:

1. The goal of proof by cases is to add extra information in each case, visible here as the extra given in each sub-proof.
2. The cases need to be exhaustive, so that the OR of all of them is equivalent to true.
    In TFL, this is ensured by adding specific proof rules (such as LEM) that only apply when this is the case.



