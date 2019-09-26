---
title: Practice problems with sets
...

Assume the following definitions:

notation            meaning
---------------     -------------------
$\mathbb{Z}$        The integers
$\mathbb{Z}^{+}$    The positive integers; i.e., $\big\{ x \; \big| \; x \in \mathbb{Z} \land x > 0 \big\}$
$\mathbb{N}$        The natural numbers; i.e., $\mathbb{Z} \cup {0}$
$\mathbb{Z}^{-}$    The negative integers; i.e., $\big\{ x \; \big| \; x \in \mathbb{Z} \land x < 0 \big\}$
$\mathbb{R}$        The real numbers
$\mathbb{Q}$        The rational numbers; i.e., $\Big\{ \frac{x}{y} \; \Big| \; x \in \mathbb{Z} \land y \in \mathbb{Z}^{+} \Big\}$
$\pi$               The ratio of the circumference of a circle to its diameter; 3.1415926535...

Assume that $\mathbb Q^{+}$, $\mathbb Q^{-}$, $\mathbb R^{+}$, and $\mathbb R^{-}$ are defined similarly to $\mathbb Z^{+}$ and $\mathbb Z^{-}$.


# Membership

## Simple membership

Each of the following is either true or false; which one?

- $3 \in \mathbb Z$^[true]
- $3.5 \in \mathbb Z$^[false]
- $\pi \in \mathbb Z$^[false]
- $3 \in \mathbb Q$^[true]
- $3.5 \in \mathbb Q$^[true]
- $\pi \in \mathbb Q$^[false]
- $3 \in \mathbb R$^[true]
- $3.5 \in \mathbb R$^[true]
- $\pi \in \mathbb R$^[true]

- $3 \in \big\{x + y \;\big|\; x,y \in \mathbb{Z}^{+} \land x > y \big\}$^[true]
- $3.5 \in \big\{x + y \;\big|\; x \in \mathbb{Z}^{+} \land y \in \mathbb{R}^{+} \big\}$^[true]
- $0 \in \big\{x + y \;\big|\; x,y \in \mathbb{Z}^{+} \land x > y \big\}$^[false]
- $0 \in \big\{x - y \;\big|\; x,y \in \mathbb{R} \land x > y \big\}$^[false]

- $3 \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$^[false]
- $\{3\} \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$^[false]
- $\{2, 3\} \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$^[true]

- $\{2, 3\} \in \mathcal{P}\big(\{2, 3\}\big)$^[true]
- $|\{2, 3\}| \in \{2, 3\}$^[true]
- $|\{2, 3\}| \in \mathcal{P}\big(\{2, 3\}\big)$^[false]
- $\infty \in \mathbb R$^[false]

## Qualified membership

Each of the following is either true or false; which one?

- $\forall x \in \mathbb R \;.\; x \in \mathbb Q$^[false]
- $\forall x \in \mathbb Q \;.\; x \in \mathbb R$^[true]
- $\forall x \in \mathbb Z^{+} \;.\; \exists y \in \mathbb Z^{-} \;.\; x + y = 0$^[true]
- $\forall x \in \mathbb R^{+} \;.\; \exists y \in \mathbb Z^{+} \;.\; 1 \leq \frac{x}{y} \leq 2$^[false]
- $\exists x \in \mathbb R \;.\; x \in \mathbb N$^[true]
- $\exists x \in \mathbb R^{+} \;.\; x \notin \mathbb Q^{+}$^[true]
- $\exists x,y \in (\mathbb R \setminus \mathbb N) \;.\; (x \neq y) \land \big((x - y) \in \mathbb N\big)$^[true]
- $\forall x \in \mathbb R \;.\; (x \in \mathbb N) \rightarrow (x \in \mathbb Z)$^[true]
- $\forall x \in \mathbb Z \;.\; (x \in \mathbb Z^{+}) \lor (x \in \mathbb Z^{-})$^[false]
- $\forall x \in \mathbb N \;.\; (x < 0) \rightarrow \bot$^[true]
- $\forall x \in \mathbb N \;.\; x \in \big\{ \lfloor y \rfloor \;\big|\; y \in \mathbb R^{+} \big\}$^[true]
- $\forall x \in \mathbb N \;.\; x + 1 \in \mathbb N$^[true]
- $\forall S \in \{\mathbb Z, \mathbb Q, \mathbb R\}\;.\; \forall x \in S \;.\; x + 1 \in S$^[true]
- $\forall x \in \{3, 1, 4, 5\} \;.\; x^{x} \in \{0, 1, 4, 27, 256, 3125, 46656\}$^[true]
- $0 \in \big\{x \;\big|\; \exists y \in \mathbb Z \;.\; y^{y} = x \big\}$^[false]
- $\Big|\big\{ x \;\big|\; (x \in \mathbb R) \land (\forall y \in \mathbb N \;.\; x > y) \big\}\Big| \in {0,1,2}$^[true]
- $8 \in \big\{x^3 \;\big|\; \exists y \in \mathbb Z \;.\; y^2 = x \big\}$^[false]
- $1 \in \big\{x^3 \;\big|\; \exists y \in \mathbb Z \;.\; y^2 = x \big\}$^[true]
- $64 \in \big\{x^3 \;\big|\; \exists y \in \mathbb Z \;.\; y^2 = x \big\}$^[true]


A set is said to be **closed over** an operation if applying that operation to members of the set always results in another member of that set.

- Which (if any, or all) of the following operators is $\mathbb Z$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>^[true]
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <lable><input type="checkbox"></input> division ($\div$)</label>^[false]
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[mostly true, except for 0 divisors]
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb N$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>^[false]
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <lable><input type="checkbox"></input> division ($\div$)</label>^[false]
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[mostly true, except for 0 divisors]
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb R^{-}$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>^[false]
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>^[false]
    - <lable><input type="checkbox"></input> division ($\div$)</label>^[false]
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[false]
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb Q$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>^[true]
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <lable><input type="checkbox"></input> division ($\div$)</label>^[mostly true, except for 0 divisors]
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[mostly true, except for 0 divisors]
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb Q \setminus \{0\}$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>^[false]
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <lable><input type="checkbox"></input> division ($\div$)</label>^[true]
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[false]
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false]

- Which (if any, or all) of the following operators is $\mathbb R$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>^[true]
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>^[true]
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>^[true]
    - <lable><input type="checkbox"></input> division ($\div$)</label>^[mostly true, except for 0 divisors]
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>^[mostly true, except for 0 divisors]
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>^[false because $\mathbb R$ contains negative numbers]



# Comparison

For each of the following, fill in the blank with the first element of the following list that applies:

- $=$ if the two are identical; otherwise
- $\subset$ or $\supset$ if those are true; otherwise
- $\subseteq$ or $\supseteq$ if those are true; otherwise
- "disjoint" if the intersection of the two is $\emptyset$; otherwise
- $\neq$

|Set 1 |  |Set 2|
|------|--|-----|
|$\mathbb R$ |<input></input>^[$\subset$] |$\mathbb Q$|
|$\mathbb N$ |<input></input>^[$\subset$] |$\mathbb Z^{+}$|
|even numbers |<input></input>^[disjoint] |odd numbers|
|prime numbers |<input></input>^[$\neq$] |odd numbers|
|$\{1, 3, 5\}$ |<input></input>^[disjoint] |$\{\{1\}, \{3\}, \{5\}\}$|
|$\{1, 3, 5\}$ |<input></input>^[=] |$\{5, 3, 1\}$|
|$\{1, 3, 5\}$ |<input></input>^[$\supset$] |$\{5, 3\}$|
|$\{0, 1\}$ |<input></input>^[=] |$\big\{ x \;\big|\; x \in \mathbb{R} \land x^2 = x\big\}$|
|$\mathbb{N}$ |<input></input>^[=] |$\Big\{ x \;\Big|\; x \in \mathbb{R}^{+} \land \big(x - \lfloor x \rfloor = 0\big)\Big\}$|
|even numbers |<input></input>^[=] |$\big\{x \;\big|\; \exists y \in \mathbb Z \;.\; 2y = x\big\}$|
|$\mathbb R \setminus \mathbb Z$|<input></input>^[=] |$\Big\{ x \;\Big|\; (x \in \mathbb R) \land \big(\forall y \in \mathbb Z \;.\; x \neq y\big) \Big\}$|
|$\mathbb R \setminus \mathbb Z$|<input></input>^[$\supset$] |$\mathbb R \setminus \mathbb Q$|
|$\mathbb Z \setminus \mathbb Q$|<input></input>^[$\subset$] |${1, 2, 4}$|
|$\emptyset$|<input></input>^[$\subset$] |$\mathcal{P}(\emptyset)$|
|${1}$|<input></input>^[disjoint] |$\mathcal{P}({1})$|
|$R^{+}$|<input></input>^[=] |$\big\{ x \;\big|\; x \in \mathbb R \land \sqrt{x^2} = x \big\}$|
