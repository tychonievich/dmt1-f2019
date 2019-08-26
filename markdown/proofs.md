---
title: On Proofs
...

A major component of this course is proofs.
There are several varieties of proof, and more than one approach and purpose to some.
The terminology on this page is intended to be instructive, not formal, and other sources (even other sources by the same author) may use different terminology or break proofs into a different set of varieties.

# Varieties of proof

## Colloquial proof

Often when people refer to "proof" they mean it is a very loose, colloquial sense to mean, roughly, "something that can convince you something is inevitably or objectively (as opposed to probably or subjectively) true."
Colloquial proofs range from an appeal to authority ("Mathematicians have shown that ...") to the key insights that would allow you to flesh out an argument in your head ("there were cookies in the jar last night, but there aren't this morning, so clearly ...").

A goal of this course is to help you develop the experience and skills needed to evaluate good and bad colloquial proofs. However, a study of this form of argument is not a primary component of this course.

## Scratchwork

Scratchwork is the notation created along the way during the construction or explanation of a proof.
Most proofs have too many steps to hold them all in your working memory at once; scratchwork serves to extend that space by keeping much of it visible in front of you and all accessible to your mind as you think.
However, it often lacks the context and clarity to be meaningful to those not present during its construction---including, notably, the future selves of those who created it. Old scratchwork has limited value.

Scratchwork will be used extensively in class presentations, and you should use it for every proof your create.
We will discuss some ways of structuring it in some situations, but it may range from sketches to tabular data to almost anything else.

## Prose proof

The final versions of high-quality proofs, as they appear in publications, are a specialized type of language arts.
Their tone, grammar, and even typeface communicate "I know what I'm doing, trust me."
Their content is a progression of steps at just the right resolution so that the target audience can see how each follows logically without seeming too obvious.
Their ordering and presentation is selected to make the conclusion feel almost inevitable.

As with other advanced language arts like poetry and novels, full prose proofs cannot be mastered in a single semester: it takes years of diligent practice to hone those skills.
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

We will spend some time working proofs at nearly machine-checkable detail in this course.

### Proof-carrying code

A special case of machine-checkable proofs is proof-carrying code.
You can think of this as being a special comment syntax containing machine-checkable proof steps that a proof checker can use to verify properties of the code.

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

# Why proofs

Some of you will end up proving things to humans, as e.g. by engaging in theoretical CS research. This course will be the first of many steps in developing that ability.

Many of you will need to evaluate putative proofs provided by others. This course will help you develop that ability.

All of you will need to be careful in your thinking and notice when you are making invalid leaps of judgment and overlooking corner cases. Working with proofs provides a fertile training ground in developing this ability.

Part of the goal of a university education is provide an understanding of the world so it ceases to be mysterious.
Many people treat proofs as mysterious and infallible; we hope this course will explore them enough that you will stop seeing them as either.
