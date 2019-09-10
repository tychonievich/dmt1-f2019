---
title: Proof Techniques
subtitle: as of Quiz 2
...

Proof techniques we've learned so far:

# Apply Equivalence Rules

> See also §3.3 and §3.4.2, as well as [our list of equivalences](axioms.html#equivalences).

In a small step proof, write an equivalent expression and cite the rule used to reach it. If several rules are needed, write them out one by one.

{.example ...} The following uses a note per line to show how it is equivalent to the preceding line

<table class="TFL">
<tr><td>1</td><td>$A \lor (B \lor C)$</td></tr>
<tr><td>2</td><td>$(A \lor B) \lor C$</td><td>Associative property of $\lor$</tr>
<tr><td>3</td><td>$(B \lor A) \lor C$</td><td>Commutative property of $\lor$</tr>
<tr><td>4</td><td>$B \lor (A \lor C)$</td><td>Associative property of $\lor$</tr>
<tr><td>5</td><td>$(\lnot (\lnot B)) \lor (A \lor C)$</td><td>Double negation</tr>
<tr><td>6</td><td>$(\lnot B) \rightarrow (A \lor C)$</td><td>Disjunction ot implication</tr>
</table>
{/}

In a prose proof, write the original and the new expression, separated by "can be re-written as" or "is equivalent to". Only include intermediate steps or identified proof rules if you believe your audience would take more than a few minutes to figure them out themselves.
Common shortcut phrases for guiding through steps include

Rearranging
:   Utilizing the associative, commutative, and distributive properties of operators

Simplifying
:   Removing double negation and the ones and zeros effects of tautologies and contradictions

{.example ...} This is the same example as the previous one, but written in prose style instead.

<div class="snippet">
$A \lor (B \lor C)$ can be re-written as $(\lnot \lnot B) \lor (A \lor C)$, which is equivalent to $(\lnot B) \rightarrow A \lor C$ by the equivalence of implication and disjuction.
</div>
{/}

# Case Analysis

> See also §1.7, ∀x 17.5, and [our proof of one of De Morgan's laws](demogan.html)

State a disjunctive tautology.
For a simple tautology like $P \lor \lnot P$, stating it is enough;
for more complicated tautologies, you may need to add a sub-proof or lemma^[a lemma is a helper proof made before the main proof it will be used inside of] that it *is* tautological.

Then proceed to consider several cases: one for each term of the disjunctive tautology, in each case assuming that that clause is true.

After completing all of the cases, the full proof is also completed:we may not know *which* case's assumption is true, but because the disjunction is a tautology, we know at least one of them *must* be.

{.example ...} This is a full proof of one of our known equivalences

<div class="theorem">
$P \rightarrow Q \equiv \lnot P \lor Q$
</div>

<div class="proof">
Either $P$ is true or $P$ is false.

Case 1: $P$ is true
:   The expression $P \rightarrow Q$ in this case is equivalent to $\top \rightarrow Q$, which can be simplified to $Q$.
    
    The expression $\lnot P \lor Q$ in this case is equivalent to $\bot \lor Q$, which can be simplified to $Q$.
    
    Since the two are equivalent to the same thing, they are equivalent to each other.

Case 2: $P$ is false
:   The expression $P \rightarrow Q$ in this case is equivalent to $\bot \rightarrow Q$, which can be simplified to $\top$.
    
    The expression $\lnot P \lor Q$ in this case is equivalent to $\top \lor Q$, which can be simplified to $\top$.
    
    Since the two are equivalent to the same thing, they are equivalent to each other.

Since $P \rightarrow Q \equiv \lnot P \lor Q$ is true in both cases, it is true in general.

</div>
{/}

Case analysis in small-step proofs involves embedded sub-proofs, as is described in ∀x 17.5 and used in ∀x 17.1 and ∀x 19.6.



