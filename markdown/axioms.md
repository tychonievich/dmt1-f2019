---
title: Axioms
...

# Equivalences

Two expressions are equivalent if they have the same truth valuation regardless of 

## Simplifications

Simplifications have the property that they make expressions smaller, with fewer operators and propositions.
They are equivalences so they also work backwards (i.e. making expressions larger), a process sometimes called "introduction", as in "we can introduce a double negation"

The first five are big and worth memorizing

 long                    simplified                 Name of rule
----------------------  ------------------------    ----------------------------
$\lnot \lnot P$         $P$                         double negation
$P \land \bot$          $\bot$
$P \land \top$          $P$
$P \lor \bot$           $P$
$P \lor \top$           $\top$

and the rest are either less commonly useful or can be derived from the five above rules


| simplified |$\rightarrow$|$\leftrightarrow$|$\oplus$|$\land$|$\lor$|
|:------:|:-----------:|:---------------:|:------:|:-----:|:----:|
|$P$|$\top \rightarrow P$<br/>$\lnot P \rightarrow P$|$\top \leftrightarrow P$|$\bot \oplus P$|$\top \land P$<br/>$P \land P$|$\bot \lor P$<br/>$P \lor P$|
|$\lnot P$|$P \rightarrow \bot$<br/>$P \rightarrow \lnot P$|$\bot \leftrightarrow P$|$\top \oplus P$|||
|$\top$|$\bot \rightarrow P$<br/>$P \rightarrow \top$<br/>$P \rightarrow P$|$P \leftrightarrow P$|$P \oplus \lnot P$||$\top \lor P$<br/>$P \lor \lnot P$|
|$\bot$||$P \leftrightarrow \lnot P$|$P \oplus P$|$\bot \land P$<br/>$P \land \lnot P$||




## Other equivalences

The following operators are both **associative** (you can add and remove parentheses around them) and **commutative** (you can swap their operands' position): $\land$, $\lor$, $\oplus$

The following operator is *commutative* but not *associative*: $\leftrightarrow$

Of the other rules here, the first several are worth memorizing

 form 1                  form 2                                         Name of rule
----------------------  -------------------------------                 ----------------------------
$A \rightarrow B$       $\lnot A \lor B$
$A \land (B \lor C)$    $(A \land B) \lor (A \land C)$                  Distributive law
$A \lor (B \land C)$    $(A \lor B) \land (A \lor C)$                   Distributive law
$\lnot (A \land B)$     $(\lnot A) \lor (\lnot B)$                      De Morgan's law
$\lnot (A \lor B)$      $(\lnot A) \land (\lnot B)$                     De Morgan's law
$(A \leftrightarrow B)$ $(A \rightarrow B) \land (B \rightarrow A)$
$(A \oplus B)$          $(A \lor B) \land \lnot (A \land B)$

and the rest are either less commonly useful or can be derived easily from other worth-memorizing rules

 form 1                      form 2                             Name of rule
----------------------      ---------------------------------   ----------------------------
$A \oplus B$                $\lnot (A \leftrightarrow B)$       
$A \leftrightarrow B$       $\lnot (A \oplus B)$                xnor
$P \rightarrow (A \lor Q)$  $(P \land \lnot A) \rightarrow Q$


# Entailments

## Set entailment

Given                                                       Entails
-------------------------------------------------------     -----------------------------
$P(x)$ and $x \in S$                                        $\exists x \in S \;.\; P(x)$
$\forall x \in S \;.\; P(x)$ and $T \subseteq S$            $\forall x \in T \;.\; P(x)$
$\exists x \in S \;.\; P(x)$ and $T \supseteq S$            $\exists x \in T \;.\; P(x)$
$\forall x \in S \;.\; P(x)$ and $S \neq \emptyset$         $\exists x \in S \;.\; P(x)$
$|S| \neq |T|$                                              $S \neq T$
$|S| < |T|$                                                 $S \not \supseteq T$
$\exists x \in S \;.\; P(x)$                                $P \neq \emptyset$


## Qualified entailments

Given                             Entails                                                               Names
--------------------------------  -----------------------------                                         ------
$\forall x \in S \;.\; P(x)$      $P(s)$, for any $s \in S$ we care to pick                             universal instantiation
$\exists x \in S \;.\; P(x)$      $s \in S \land P(s)$ where $s$ is an otherwise-undefined new variable existential instantiation 
$s \in S \vdash P(s)$             $\forall x \in S \;.\; P(x)$                                          universal generalization
$P(s) \land s \in S$              $\exists x \in S \;.\; P(x)$                                          existential generalization

These also all have versions that use a defined domain instead of set membership.
Universal generalization is sometimes called "skolemization."

## Logical entailment

Given                                                       Entails                         Name
-------------------------------------------------------     -----------------------------   --------------------
$\bot$                                                      ${x}$
                                                            ${\top}$
                                                            ${A \lor \lnot A}$              excluded middle
$A \land B$                                                 ${A}$
$A$ and $B$                                                 ${A \land B}$
$A$                                                         ${A \lor B}$
$A \lor B$ and $\lnot B$                                    ${A}$                           disjuctive syllogism
$A \rightarrow B$ and $B \rightarrow C$                     ${A \rightarrow C}$             hypothetical syllogism; transitivity of implication
$A \rightarrow B$ and $A$                                   ${B}$                           modus ponens
$A \rightarrow B$ and $\lnot B$                             ${\lnot A}$                     modus tolens
$A \leftrightarrow B$                                       ${A \rightarrow B}$
${A \rightarrow C}$, ${B \rightarrow B}$, and ${A \lor B}$  ${C}$
${A \rightarrow B}$, ${C \rightarrow D}$, and ${A \lor C}$  ${B \lor D}$
$A \rightarrow B$                                           ${A \rightarrow (A \land B)}$
$\lnot(A \land B)$, $A$                                     ${\lnot B}$

## Assume-and-prove entailment

A proof that assumes $A$ and derives $B$ entails that $A \rightarrow B$. This is commonly used in the inductive step of a proof by contradiction.

A proof that assumes $A$ and derives $\bot$ entails that $\lnot A$. This is called "proof by contradiction" or "indirect proof."


# Mathematical Identities

The following are all true for all real numbers where both sides of the equals sign are defined:

- $\displaystyle \log_a(a^x) = x$
- $\displaystyle a^{\log_a(x)} = x$
- $\displaystyle \log_a(x y) = \log_a(x) + \log_a(y)$
- $\displaystyle \log_a\left(\frac{x}{y}\right) = \log_a(x) - \log_a(y)$
- $\displaystyle \log_a(x^y) = y \log_a(x)$
- $\displaystyle \log_a(x) = \frac{\log_b(x)}{\log_b(a)}$
- $\displaystyle \log_{a^b}(x) = b^{-1}\log_a(x)$

The following are also true:

- $(a \in \mathbb Z) \land (a > 1) \vDash (a$ has at least two factors$)$
- $(a \in \mathbb Z) \land (a > 1) \land (a$ has exactly two factors$) \equiv (a$ is prime$)$
- Each integer greater than 1 has exactly one prime factorization
