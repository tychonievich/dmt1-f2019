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

> See also §1.7, ∀x 17.5, and [our proof of one of De Morgan's laws](demorgan.html)

1. State a disjunctive tautology.
For a simple tautology like $P \lor \lnot P$, stating it is enough;
for more complicated tautologies, you may need to add a sub-proof or lemma^[a lemma is a helper proof made before the main proof it will be used inside of] that it *is* tautological.

2. Then proceed to consider several cases: one for each term of the disjunctive tautology, in each case assuming that that clause is true.

3. After completing all of the cases, the full proof is also completed:we may not know *which* case's assumption is true, but because the disjunction is a tautology, we know at least one of them *must* be.

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

# Apply Entailment

> See also [our list of entailments](axioms.html#entailments).


Applying entailment is very much like applying equivalence rule, except it only needs to work in one direction.
Because $A \equiv B$ implies $A \vDash B$, you can use equivalence rules in a proof that applies entailment.

There are many more entailments (sometimes called "proof rules" or "inference rules") than there are equivalence rules, so using them can make proof construction much easier than limiting yourself to equivalences.

A proof that only uses proof rules is sometimes called a *direct proof*.


# Proof by Contradiction

1. Assume the negation of what you want to prove.
2. Use other proof techniques to derive $\bot$.
3. State "because assuming $\lnot A$ led to a contradiction, $A$ must be true" or the equivalent in other words.

{.example ...} 
<div class="theorem">
There is no largest real number.
</div>

<div class="proof">
Assume there is a largest real number.
Call that largest real number $x$; because it is the largest, we know that
$$\tag{1} \forall y \in \mathbb R \;.\; y \le x $$

Consider the number $x+1$.
Because $x$ and $1$ are both real numbers and the reals are closed over addition,
$x+1 \in \mathbb R$.
Thus, we can instantiate $(1)$ with $y = x+1$ to get $x+1 \le x$.
But clearly $x+1 > x$, which is a contradiction.

Because assuming there is a largest real number led to a contradiction, there must be no largest real number.
</div>
{/}

# Proof by Induction

Proof by induction, in its purest form, only works for theorems of the form $\boxed{\forall n \in \mathbb N \;.\; P(n)}$ where $P$ is a predicate.
However, many other proofs can be [reduced](reducibility.html) to that form.

1. State you are using induction.
2. Identify one or more base cases, which are $P(0)$ and (if needed) $P(1)$, $P(2)$, etc.; prove each using other proof techniques.
3. Add an inductive step of the form "assume $P(n)$" and then prove $P(n+1)$; if needed, you can assume $\boxed{\forall i \in \big\{ i \;\big|\; i \in \mathbb N \land i \le n \} \;.\; P(i)}$ instead (called "strong induction") if needed.
4. State that by the principle of induction, the theorem holds for all $n \in \mathbb N$.

{.example ...}
<div class="theorem">
$\mathbb N \subseteq \mathbb R$
</div>

Note that by the definition of subsets, this is equivalent to proving $\boxed{\forall n \in \mathbb N \;.\; n \in \mathbb R}$, so we'll use $P(n) = n \in \mathbb R$ as our predicate.

<div class="proof"> We proceed by induction.

Base case
:   $0 \in \mathbb R$ by definition.

Inductive case
:   Assume $n \in \mathbb N$ and $n \in \mathbb R$.
    Consider $x = n+1$;
    because $1 \in \mathbb R$ and the reals are closed under addition, $x \in \mathbb R$.

By the principle of induction, it follows that $\forall n \in \mathbb N \;.\; n \in \mathbb R$.
By the definition of subsets, that means $\mathbb N \subseteq \mathbb R$.
</div>
{/}

Induction is used so often that the template is often applied with fairly dramatic modifications, possibly even having multiple inductive steps, without explicitly noting those modifications.

{.example ...}
<div class="theorem">
If a string is created by starting with "`a`" and optionally replacing an "`a`" with "`ab`" or a "`b`" with "`aa`", as many times as you want, the result will always have an odd number of "`a`"s.
</div>

It is also true that any string consisting of an odd number of `a`s, each followed by any number of `b`s, can be created with this process, but let's start with this easier odd-number proof first.

<div class="proof"> We proceed by induction.

Base case
:   "`a`" has one "`a`", which is an odd number.

Inductive case
:   Assume a string $s$ has an odd number of "`a`"s.
    Consider the a string $t$ created in one step from $s$.
    
    Case `a` to `ab`
    :   Suppose $t$ was created by replacing one "`a`" in $s$ with "`ab`".
        $t$ has the same number of "`a`"s as $s$, so by our assumption $t$ has an odd number of "`a`"s.
        
    Case `b` to `aa`
    :   Suppose $t$ was created by replacing one "`b`" in $s$ with "`aa`".
        $t$ has exactly two more "`a`"s than $s$, and 2 + an odd number is still odd, so by our assumption $t$ has an odd number of "`a`"s.
    
    Since $t$ has an odd number of "`a`"s in each case, it has an odd numebr of "`a`"s in general.

By the principle of induction, it follows that all strings created using this process have an odd number of "`a`"s.
</div>

Implicitly, the above proof used induction on the number of steps used to create the string, but that was never identified in the proof itself.
{/}
