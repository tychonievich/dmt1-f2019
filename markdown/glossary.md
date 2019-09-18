---
title: Glossary of logical terms
...

See also our [list of symbols](symbols.html)

Antecedent
:   The left-hand operand of a conditional; the $X$ is $X \rightarrow Y$.

Axiom
:   Something we accept as true without requiring a proof.

Associative
:   Of an operator, meaning the order of operations when several of that operator are applied in a row does not matter.
    To say some operator $\cdot$ is associative means that $(P \cdot Q) \cdot R \equiv P \cdot (Q \cdot R)$ for all propositions $P$, $Q$, and $R$.

Biconditional
:   See *Iff*.

Bi-implication
:   See *Iff*.

Commutative
:   Of an operator, meaning the order of its operands does not matter.
    To say some operator $\cdot$ is commutative means that $P \cdot Q \equiv Q \cdot P$ for all propositions $P$ and $Q$.

Conjunction
:   Logical AND ($\land$).

Consequent
:   The right-hand operand of a conditional; the $Y$ is $X \rightarrow Y$.

Contradiction
:   A logical expression that is equivalent to FALSE ($\bot$).

De Morgan's laws
:   Two specific, related logical equivalences; see our [list of equivalences](axioms.html#equivalences) for their form.
    
    Because of their related structure, it is not uncommon to refer to both together in the singular (i.e. "De Morgan's law").

Disjunction
:   Logical OR ($\lor$).

Domain
:   The possible values a variable could take under a quantifier; for example, if the domain is "all animals" then $\forall x \;.\; F(x)$ means "$F$ is true for all animals".

Equivalent
:   Two logical expressions $P$ and $Q$ are equivalent if and only if the expression $P \leftrightarrow Q$ is a tautology.

Formula
:   see *Logical Expression*.

Iff
:   A contraction of "if and only if", a name for the operator $\leftrightarrow$.

Logical Expression
:   One or more propositions or predicates, combined with operators so that the whole is a predicate or proposition.

Necessary
:   Cannot happen without. If $A$ is a necessary condition for $B$, then we know both

    - Without $A$, no $B$ is possible. $\lnot A \rightarrow \lnot B$
    - If you see $B$, $A$ must also be. $B \rightarrow A$
    
    Often used to suggest partial causation or a requirement. Compare *Sufficient*.

Predicate
:   A single word for two related concepts:
    
    - In logic, an incomplete proposition, where one or more component has been replaced by a *Variable*.
    - In programming, a subroutine that (a) has no side-effects and (b) always returns a Boolean value.

Proposition
:   A statement that, by construction, must either be true or false.

Quantifier
:   One of $\forall$ or $\exists$; some people also include $\nexists$ while others think of that as being shorthand for $\lnot \exists$.

Satisfiable
:   A satisfiable expression is not a contradiction.

Sentence
:   see *Logical Expression*.

Sufficient
:   Always happens if. If $A$ is a sufficient condition for $B$, then we know both

    - If you see $A$, $B$ must also be. $A \rightarrow B$
    - If you don't see $B$, $A$ can't be. $\lnot B \rightarrow \lnot A$

    Often used to suggest causation. Compare *Necessary*.

Tautology
:   A logical expression that is equivalent to TRUE ($\top$).

Universe of Discourse
:   see *Domain*.

Variable
:   A single word for (at least) three concepts with similar but non-identical meaning:
    
    - In algebra, a place-holder for a single numeric value.
    - In logic, a place-holder for a single element from the *Domain*, generally used with *Quantifiers* and *Predicates*.
    - In programming, a named region of memory that may take different values at different times.
    
