---
title: Symbols we'll use
...

You have enough to worry about memorizing without keeping dozens of symbols in your head at once. We intend to provide this table for your reference during every in-class evaluation.

Concept          Java/C      Python      This class                      Bitwise    Other
--------        --------    --------    ---------------------------     ---------   ------
true            `true`      `True`      $\top$ or $1$                   `-1`        T, tautology
false           `false`     `False`     $\bot$ or $0$                   `0`         F, contradiction
not $P$         `!p`        `not p`     $\lnot P$ or $\overline{P}$     `~p`
$P$ and $Q$     `p && q`    `p and q`   $P \land Q$                     `p & q`     $P Q$, $P \cdot Q$
$P$ or $Q$      `p || q`    `p or q`    $P \lor Q$                      `p | q`     $P + Q$
$P$ xor $Q$     `p != q`    `p != q`    $P \oplus Q$                    `p ^ q`     $P ⊻ Q$
$P$ implies $Q$                         $P \rightarrow Q$                           $P \supset Q$, $P \Rightarrow Q$
$P$ iff $Q$     `p == q`    `p == q`    $P \leftrightarrow Q$                       $P \Leftrightarrow Q$, $P$ xnor $Q$, $P \equiv Q$


Concept          Symbol         Meaning
--------        --------        --------------
equivalent      $\equiv$        "$A \equiv B$" means "$A \leftrightarrow B$ is a tautology"
entails         $\vDash$        "$A \vDash B$" means "$A \rightarrow B$ is a tautology"
provable        $\vdash$        "$A \vdash B$" means both "$A \vDash B$" and "I know $B$ is true because $A$ is true"<br/>"$\vdash B$" (i.e., without $A$) means "I know $B$ is true"
therefore       $\therefore$    "$\therefore A$" means both "$\vdash A$" and "$A$ is the thing we wanted to show"

