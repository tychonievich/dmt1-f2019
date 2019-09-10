---
title: Axioms
...

# Equivalences

Two expressions are equivalent if they have the same truth valuation regardless of 

## Simplifications

Simplifications have the property that they make expressions smaller, with fewer operators and propositions.
They are equivalences so they also work backwards (i.e. making expressions larger), a process sometimes called "introduction", as in "we can introduce a double negation"

The first five are big and worth memorizing

 long                    simplified                 Name of rule (if any)
----------------------  ------------------------    ----------------------------
$\lnot \lnot P$         $P$                         double negation
$P \land \bot$          $\bot$
$P \land \top$          $P$
$P \lor \bot$           $P$
$P \lor \top$           $\top$

and the rest are either less commonly useful or can be derived easily from other worth-memorizing rules

 long                        simplified            Name of rule (if any)
----------------------      --------------------   ----------------------------
$P \rightarrow \bot$        $\lnot P$              The proof-rule version is called "modus tollens"
$P \rightarrow \top$        $\top$
$\bot \rightarrow P$        $\top$
$\top \rightarrow P$        $P$                    The proof-rule version is called "modus ponens"
$P \leftrightarrow \bot$    $\lnot P$
$P \leftrightarrow \top$    $P$
$P \oplus \bot$             $P$
$P \oplus \top$             $\lnot P$

## Other equivalences

The following operators are both **associative** (you can add and remove parentheses around them) and **commutative** (you can swap their operands' position): $\land$, $\lor$, $\oplus$, $\leftrightarrow$

Of the other rules here, the first four are worth memorizing

 form 1                  form 2                                         Name of rule (if any)
----------------------  -------------------------------                 ----------------------------
$A \land (B \lor C)$    $(A \land B) \lor (A \land C)$                  Distributive law
$A \lor (B \land C)$    $(A \lor B) \land (A \lor C)$                   Distributive law
$\lnot (A \land B)$     $(\lnot A) \lor (\lnot B)$                      De Morgan's law
$\lnot (A \lor B)$      $(\lnot A) \land (\lnot B)$                     De Morgan's law
$(A \leftrightarrow B)$ $(A \rightarrow B) \land (B \rightarrow A)$
$(A \oplus B)$          $(A \lor B) \land \lnot (A \land B)$

and the rest are either less commonly useful or can be derived easily from other worth-memorizing rules

 form 1                      form 2                             Name of rule (if any)
----------------------      ---------------------------------   ----------------------------
$A \oplus B$                $\lnot (A \leftrightarrow B)$       
$A \leftrightarrow B$       $\lnot (A \oplus B)$                xnor
$P \rightarrow (A \lor Q)$   $(P \land \lnot A) \rightarrow Q$
