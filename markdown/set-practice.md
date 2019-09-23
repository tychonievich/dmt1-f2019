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

- $3 \in \mathbb Z$
- $3.5 \in \mathbb Z$
- $\pi \in \mathbb Z$
- $3 \in \mathbb Q$
- $3.5 \in \mathbb Q$
- $\pi \in \mathbb Q$
- $3 \in \mathbb R$
- $3.5 \in \mathbb R$
- $\pi \in \mathbb R$

- $3 \in \big\{x + y \;\big|\; x,y \in \mathbb{Z}^{+} \land x > y \big\}$
- $3.5 \in \big\{x + y \;\big|\; x \in \mathbb{Z}^{+} \land y \in \mathbb{R}^{+} \big\}$
- $0 \in \big\{x + y \;\big|\; x,y \in \mathbb{Z}^{+} \land x > y \big\}$
- $0 \in \big\{x - y \;\big|\; x,y \in \mathbb{Z}^{+} \land x > y \big\}$

- $3 \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$
- $\{3\} \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$
- $\{2, 3\} \in \{\{1\}, \{2, 3\}, \{4, 5, 6\}\}$

## Qualified membership

Each of the following is either true or false; which one?

- $\forall x \in \mathbb R \;.\; x \in \mathbb Q$
- $\forall x \in \mathbb Q \;.\; x \in \mathbb R$
- $\forall x \in \mathbb Z^{+} \;.\; \exists y \in \mathbb Z^{-} \;.\; x + y = 0$
- $\forall x \in \mathbb R^{+} \;.\; \exists y \in \mathbb Z^{+} \;.\; 1 \leq \frac{x}{y} \leq 2$
- $\exists x \in \mathbb R \;.\; x \in \mathbb N$
- $\exists x \in \mathbb R^{+} \;.\; x \notin \mathbb Q^{+}$
- $\exists x,y \in \mathbb R \;.\; (x \neq y) \land \big((x - y) \in \mathbb N\big)$
- $\forall x \in \mathbb R \;.\; (x \in \mathbb N) \rightarrow (x \in \mathbb Z)$
- $\forall x \in \mathbb Z \;.\; (x \in \mathbb Z^{+}) \lor (x \in \mathbb Z^{-})$
- $\forall x \in \mathbb N \;.\; (x < 0) \rightarrow \bot$
- $\forall x \in \mathbb N \;.\; x \in \big\{ \lfloor y \rfloor \;\big|\; y \in \mathbb R^{+} \big\}$
- $\forall x \in \mathbb N \;.\; x + 1 \in \mathbb N$
- $\forall S \in \{\mathbb Z, \mathbb Q, \mathbb R\}\;.\; \forall x \in S \;.\; x + 1 \in \mathbb S$
- $\forall x \in \{3, 1, 4, 5\} \;.\; x^{x} \in \{0, 1, 4, 27, 256, 3125, 46656\}$
- $0 \in \big\{x \;\big|\; \exists y \in \mathbb Z \;.\; y^{y} = x \big\}$


A set is said to be **closed over** an operation if applying that operation to members of the set always results in another member of that set.

- Which (if any, or all) of the following operators is $\mathbb Z$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>
    - <lable><input type="checkbox"></input> division ($\div$)</label>
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>
- Which (if any, or all) of the following operators is $\mathbb N$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>
    - <lable><input type="checkbox"></input> division ($\div$)</label>
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>
- Which (if any, or all) of the following operators is $\mathbb R^{-}$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>
    - <lable><input type="checkbox"></input> division ($\div$)</label>
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>
- Which (if any, or all) of the following operators is $\mathbb Q$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>
    - <lable><input type="checkbox"></input> division ($\div$)</label>
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>
- Which (if any, or all) of the following operators is $\mathbb Q \setminus \{0\}$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>
    - <lable><input type="checkbox"></input> division ($\div$)</label>
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>
- Which (if any, or all) of the following operators is $\emptyset$ closed over?
    - <lable><input type="checkbox"></input> addition ($+$)</label>
    - <lable><input type="checkbox"></input> subtraction ($-$)</label>
    - <lable><input type="checkbox"></input> multiplication ($\times$)</label>
    - <lable><input type="checkbox"></input> division ($\div$)</label>
    - <lable><input type="checkbox"></input> modulo ($\mod{}$ in math, `%` in code)</label>
    - <lable><input type="checkbox"></input> root extraction ($\sqrt{}$)</label>



# Comparison

For each of the following, fill in the blank with the first element of the following list that applies:

- $=$ if the two are identical; otherwise
- $\subset$ or $\supset$ if those are true; otherwise
- $\subseteq$ or $\supseteq$ if those are true; otherwise
- "disjoint" if the intersection of the two is $\emptyset$; otherwise
- $\neq$

Set 1                               Set 2
--------------  -----------------   -----------------------------
$\mathbb R$     <input></input>     $\mathbb Q$
$\mathbb N$     <input></input>     $\mathbb Z^{+}$
even numbers    <input></input>     odd numbers
prime numbers   <input></input>     odd numbers
$\{1, 3, 5\}$   <input></input>     $\{\{1\}, \{3\}, \{5\}\}$
$\{1, 3, 5\}$   <input></input>     $\{5, 3, 1\}$
$\{1, 3, 5\}$   <input></input>     $\{5, 3\}$
$\{0, 1\}$      <input></input>     $\big\{ x \;\big|\; x \in \mathbb{R} \land x^2 = x\big\}$
$\mathbb{N}$    <input></input>     $\Big\{ x \;\Big|\; x \in \mathbb{R} \land \big(x - \lfloor x \rfloor = 0\big)\Big\}$
even numbers    <input></input>     $\big\{x \;\big|\; \exists y \in \mathbb Z \;.\; 2y = x\big\}$

