---
title: On Proofs
...

A major component of this course is proofs.
There are several varieties of proof, and more than one approach and purpose to some.
The terminology on this page is intended to be instructive, not formal, and other sources (even other sources by the same author) may use different terminology or break proofs into a different set of varieties.

# Varieties of proof

## Colloquial proof

Often when people refer to "proof" they mean it is a very loose, colloquial sense to mean, roughly, "something that can convince you something is inevitably or objectively (as opposed to probably or subjectively) true."
Colloquial proofs include 

Fallacies
:   Arguments some people accept as proofs, but which are actually unsound.
    There are [many](https://en.wikipedia.org/wiki/List_of_fallacies) varieties of fallacy.
    
    {.example} I have a Ph.D. and you don't, so if we disagree I'm right and you are wrong

Hand-waving proofs
:    Arguments that skip a lot of material, implying that it is tedious to verify and I did the tedium so you don't have too.
    
    {.example ...} From [wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture#Cycle_length):
    
    the period $p$ of any non-trivial cycle of the Collatz function is of the form
    $$p = 301994 a + 17087915 b + 85137581 c$$
    where $b\geq 1$ and $a c = 0$. This result is based on the continued fraction expansion of $\log 3 / \log 2$.
    {/}

Proof outlines
:   Arguments that are intended to include the main ideas that could be used to create a proof.
    
    {.example ...}
    All primes greater than 3 are exactly one away from a multiple of 6. This is because any number $(6n+i)$, where $i$ is one of $\{0, 2, 3, 4\}$, has either 2 or 3 as a factor.
    {/}
    
    Note that what might look like a proof outline to one audience might look like a [prose proof](#prose-proof) to another audience with more experience in the domain.

A goal of this course is to help you develop the experience and skills needed to evaluate good and bad colloquial proofs. However, a study of this form of argument is not a primary component of this course.

## Whiteboard proof

Most proofs have too many steps to hold them all in your working memory at once.
Whether creating such a proof or trying to understand one someone else created,
it can be useful to create a whiteboard proof version of it.
Whiteboard proofs contain all of the components of a proof, written (or drawn or otherwise represented) outside you head so you don't have to worry about forgetting them, but lack the context and polish to be meaningful to those not present during their construction---including, notably, the future selves of those who created it.
Once you've created or understood the prose proof, you erase the board, because whiteboard proofs are a means to an end, not an end in themselves.

Whiteboard proofs will be used extensively in class presentations, and you should create them first every time you go to write a proof.
Because they are only for the benefit of those working on the proof, they do not need to abide by any particular style or structure.
That said, we will show a few patterns of whiteboard proofs in class that you might find useful to use yourself.

## Prose proof

The final versions of high-quality proofs, as they appear in publications, are a specialized type of language arts.
Their tone, grammar, and even typeface communicate "I know what I'm doing, trust me."
Their content is a progression of steps at just the right resolution so that the target audience can see how each follows logically without seeming too obvious.
Their ordering and presentation is selected to make the conclusion feel almost inevitable.

{.example ...} The theorem "There are infinitely many primes" can be proven as follows:

:::proof
Let $P$ be the set of all primes. Assume that $|P|$ is finite
and define $p_p$ as $$p_p \triangleq \prod_{x \in P} x$$
Let $p'$ be $p_p + 1$.
Then $p'$ must not have any factor in $P$ because $p' = 1 \mod p$ for every $p \in P$.
Hence either $p'$ is a prime not in $P$, or it has as a factor a different prime not in $P$.
But this contradicts our definition of $P$, so our assumption must be false, meaning $|P|$ is not finite.
:::
{/}

<!--
clear to a skeptic
not obvious but inevitable
-->


As with other advanced forms of language arts, such as poetry and novels, full prose proofs cannot be mastered in a single semester: it takes years of diligent practice to hone those skills.
However, we can and will spend time both reading and writing them in class, treating this class, in part, as an introduction to this art form.

## Machine-checkable proof

A machine-checkable proof is a sequence of small, detailed steps taken from a very restricted vocabulary of proof steps.
They are designed to allow the rapid conveyance of certainty of very large thoerems:
rapid and large because computers are fast,
certainty because they are made of such simple steps that humans can read, understand, and believe their checkers easily.

{.aside ...}
I had originally intended to have building a proof checker as a major component of this course. I wrote several 100-lines-of-code example implementations to make sure it was doable, and I think most of you would find it easily within your grasp.

However, all my reference solutions required some recursion, and knowledge of how to program recursion is not an official prerequisite of this course.
Hence, it is not listed as an assignment in this course offering.
{/}

We will spend some time working proofs at nearly machine-checkable detail in this course, and might have you work with a proof checker for a few exercises.

{.example ...} The following is a machine-checkable variant of the derivation given in ∀x 19.6, proving that $\lnot(A \land B)$ implies $\lnot A \lor \lnot B$:


<table class="TFL">
    <tr><td>1</td><td>$\lnot(A \land B)$</td></tr>
    <tr class="then"><td>2</td><td>
        <table class="TFL">
            <tr><td>2</td><td>$A$</td></tr>
            <tr class="then"><td>3</td><td>
                <table class="TFL">
                    <tr><td>3</td><td>$B$</td></tr>
                    <tr class="then"><td>4</td><td>$A \land B$</td><td>$\land$I 2, 3</td></tr>
                    <tr><td>5</td><td>$\perp$</td><td>$\lnot$E 1, 4</td></tr>
                </table>
            </td></tr>
            <tr><td>4</td><td>$\lnot B$</td><td>$\lnot$I 3</td></tr>
            <tr><td>5</td><td>$\lnot A \lor \lnot B$</td><td>$\lor$I 4</td></tr>
        </table>
    </td></tr>
    <tr><td>3</td><td>
        <table class="TFL">
            <tr><td>3</td><td>$\lnot A$</td></tr>
            <tr class="then"><td>4</td><td>$\lnot A \lor \lnot B$</td><td>$\lor$I 3</td></tr>
        </table>
    </td></tr>
    <tr><td>4</td><td>$\lnot A \lor \lnot B$</td><td>LEM 2, 3</td></tr>
</table>

Of course, to actually be checkable by machine it would not be presented visually like this, but the level of detail above is machine-checkable.
{/}

### Proof-carrying code

A special case of machine-checkable proofs is proof-carrying code.
Proof-carrying code consists of three parts:

- Code
- Assertions about the code, such as "this list index is never out of bounds"
- Machine-checkable proofs of those assertions

All three are transferred together, as e.g. by embedding the assertions and proofs in specially formatted comments.

Type-checking of statically-typed languages like C and Java is a very limited special case of machine-checkable proofs:
saying `int x`{.java} is an assertion that all subsequent lines that begin `x =` will have an `int` on the right-hand side,
and type systems are designed so that proof steps are implicit in the language specification itself.

While we will discuss some proofs of code in this course,
and many more such proofs in courses that follow it,
our curriculum does not use proof-carrying code directly.

## Computer-assisted proof

Creating proofs is hard.
Not just hard in a fuzzy human sense; provably hard.
One corollary of [Rice's Theorem](https://en.wikipedia.org/wiki/Rice%27s_theorem)
is that for *any* feature you might want to prove about a computer program
(e.g., "it does not email rude things to all my contacts and then erase my entire disk")
there exist programs that both (a) have the feature and (b) no automated process can prove has the feature.

However, we have computer programs that can do a lot toward automating proofs; coupled with human creativity and intuition, these can result in much more complex and detailed proofs than either computer or human can (efficiently) do alone.
These proof assistant tools generally take input in the form of major proof steps and decisions, and can output various forms ranging from [machine-checkable](#machine-checkable-proofs) lists of small, simple steps
to a rough draft of a [prose proof](#prose-proof).

Another variant of this course at UVA makes use of a proof assistant tool ([L∃∀N](https://leanprover.github.io)), which allows the course to be more formal and explore a large scope of proofs.
This variant of the course does not use any such tool.

Computers can also assist in creating proofs that as simply too large for humans to handle, verifying by brute force that every one of many thousands of cases individually work out.
Several significant theorems have been proven this way, perhaps most famously the [four color theorem](https://en.wikipedia.org/wiki/Four_color_theorem).

# Why proofs

Some of you will end up proving things to humans, as e.g. by engaging in theoretical CS research. This course will be the first of many steps in developing that ability.

Many of you will need to evaluate putative proofs provided by others. This course will help you develop that ability.

All of you will need to be careful in your thinking and notice when you are making invalid leaps of judgment and overlooking corner cases. Working with proofs provides a fertile training ground in developing this ability.

Part of the goal of a university education is provide an understanding of the world so it ceases to be mysterious.
Many people treat proofs as mysterious and infallible; we hope this course will explore them enough that you will stop seeing them as either.
