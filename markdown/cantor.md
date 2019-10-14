---
title: Cantor Diagonalization
...


# The Proof

:::theorem
$|\mathbb N| < |\mathbb R|$
:::

Before we get to the main proof, let's do a lemma:

:::lemma
$|\mathbb N| \leq |\mathbb R|$
:::

The lemma is easily proven by showing a total injection:

:::proof
Consider the function $f : \mathbb N \rightarrow \mathbb R$ defined as $f(x) = x$.
The function $f$ is total (it is defined for all $x \in \mathbb N$)
and injective $\big(f(x) = f(y)\big) \rightarrow (x = y)$.
Hence, there exists a total injection from $\mathbb N$ to $\mathbb R$,
which means $|\mathbb N| \leq |\mathbb R|$
:::

With this lemma, all we need to prove that $|\mathbb N| < |\mathbb R|$
is to prove that $|\mathbb N| \neq |\mathbb R|$.

:::proof
We proceed by contradiction.

Assume $|\mathbb N| = |\mathbb R|$.
Then there exists a total invertible function $f : \mathbb N \rightarrow \mathbb R$.
Let $f'$ be one such function.

Let $x \in \mathbb R$ be defined such that the $n$th digit of $x$ is one more than the $n$th digit of $f'(n)$. Formally, that means:

$$x = \sum_{n \in \mathbb N} \Big(\big\lfloor f'(n) 10^{n}\big\rfloor + 1 \mod 10\Big) 10^{-n}$$

Because $x$ is a real number and $f'$ is invertible,
there must exist some $n_x \in \mathbb N$ such that $f'(n_x) = x$.
But by construction the $n_x$th digit of $x$ differs from the $n_x$th digit of $f'(n_x)$; formally, that is

$$\big\lfloor x 10^{n_x}\big\rfloor = \big\lfloor f'(n_x) 10^{n_x}\big\rfloor + 1 \mod 10$$

That means $f'(n_x) \neq x$, which contradicts our definition of $f'$ and $n_x$.

Because assuming $|\mathbb N| = |\mathbb R|$ led to a contradiction, it must be the case that $|\mathbb N| \neq |\mathbb R|$.

Because of our lemma, we know that $|\mathbb N| \leq |\mathbb R|$, which must mean $|\mathbb N| < |\mathbb R|$
:::

# Discussion

Why does the above proof technique not work for integers?
Because if we try to apply it to integers, we end up with an infinite string of digits on the left side of the decimal point, which is not an integer.

Why does the above proof technique not work for rationals?
Because the decimal expansion of any rational repeats, and the diagonal construction of $x$ does not repeat, and thus is not rational.

There is no magic to the specific $x$ we picked; it would just as well to do a different base, like binary

$$x_1 = \sum_{n \in \mathbb N} \Big( 1 - \big\lfloor f'(n) 2^{n}\big\rfloor\Big) 2^{-n}$$

or to use a different digit-changing rule like

$$x_2 = \sum_{n \in \mathbb N} \Big( 9 - \big\lfloor f'(n) 10^{n}\big\rfloor\Big) 10^{-n}$$

or to grab a different set of digits

$$x_3 = \sum_{n \in \mathbb N} \Big(\big\lfloor f'(n) 10^{n + 2(n \mod 2)}\big\rfloor + 1 \mod 10\Big) 10^{-n - 2(n \mod 2)}$$

etc.
