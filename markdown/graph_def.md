---
title: Graph Definitions
...

<style> table ul { margin: 0; } </style>

You have enough to worry about memorizing without keeping all these terms in your head. We intend to provide this list for your reference during every in-class evaluation relating to graphs.

+-----------+-----------------------------------------------+
|Term       |Definition                                     |
+===========+===============================================+
|Walk       |An alternating sequence of vertices and edges  |
|           |                                               |
|           |- starting and ending with a vertex,           |
|           |- each edge $(x,y)$ in the walk                |
|           |   follows vertex $x$ and                      |
|           |   is followed by vertex $y$                   |
+-----------+-----------------------------------------------+
|Path       |A walk that does not visit any vertex twice    |
+-----------+-----------------------------------------------+
|Closed Walk|A walk that begins and ends at the same vertex |
+-----------+-----------------------------------------------+
|Cycle      |A closed walk that is a path                   |
|           |except for its last vertex                     |
+-----------+-----------------------------------------------+

The related definitions on relations $R : A \rightarrow A$ are

Term                Definition
-----               ------------------------------------------------------------------------
R is Reflexive      $\forall x \in A \;.\; x$ R $x$
R is Irreflexive    $\forall x \in A \;.\; \lnot(x$ R $x)$
R is Symmetric      $\forall x,y \in A \;.\; (x$ R $y) \rightarrow (y$ R $x)$
R is Asymmetric     $\forall x,y \in A \;.\; (x$ R $y) \rightarrow \lnot(y$ R $x)$
R is Antisymmetric  $\forall x \neq y \in A \;.\; (x$ R $y) \rightarrow \lnot(y$ R $x)$
R is Transitive     $\forall x,y,z \in A \;.\; (x$ R $y) \land (y$ R $z) \rightarrow (x$ R $z)$

And those lead to these terms:

Term                    Definition
-----                   ------------------------------------------------------------------------
Strict partial order    transitive and asymmetric
Weak partial order      transitive, reflexive, and antisymmetric
Equivalence relation    transitive, reflexive, and symmetric
