# Summary

This repository holds the numerical experiments
performed in [1].
On an open and bounded polygonal domain
$\Omega \subset \mathbb{R}^2$, which will be either
chosen to be the _L-shaped domain_
$\Omega_{\text{L}} := (-1, 1)^2 \setminus ([0,1] \times [-1, 0])$,
or the _square domain_ $\Omega_{\text{S}} := (0, 1)^2$,
we consider the numerical
solution of the semilinear elliptic diffusion-reaction
boundary value problem (BVP):

$$
-\nabla \cdot
\left(
    \mathbf{A} (\mathbf{x}) \nabla u(\mathbf{x})
\right)
+\phi(u(\mathbf{x}))
    =
f(\mathbf{x}),
\mathbf{x} \in  \Omega
$$

with homogeneous dirichlet boundary conditions
$u(\mathbf x) = 0$, $\mathbf x \in \partial \Omega$.
Here, $\phi \in \mathrm{C}^0(\mathbb{R})$ is non-decreasing,
$f\in \mathrm{L^2}(\Omega)$,
and $\mathbf A : \Omega \to \mathbb R^{2\times 2}$
is a piecewise constant symmetric diffusion matrix that
is uniformly positive definite,
i.e. there exists a constant $C>0$ such that

$$
\forall \mathbf{x} \in \Omega
\,:\,
\inf_{
    \substack{
        \mathbf{\xi} \in \mathbb{R}^2
        \\
        \mathbf{\xi} \neq \mathbf{0}}
    }
\frac{
    \mathbf{\xi}^\intercal\mathbf{A} (\mathbf{x})\mathbf{\xi}
}{
    \mathbf{\xi}^\intercal\mathbf{\xi}
}
\ge C.
$$

As in the paper, experiments are divided into _linear_ and
_nonlinear_ experiments corresponding to either
$\phi(u) = cu(x)$ with $c \in \{0, 1\}$ constant
or $\phi$ monotonically increasing.

## Usage
Both folders `linear_experiments` and `nonlinear_experiments`
hold files `.python-version` and `requirements.txt`
providing all necessary information for generating
the corresponding virtual environments.

## Contact
If you run into problems or have questions,
please do not hesitate to contact
[me](https://leuraph.github.io/).

# References
[1] https://arxiv.org/abs/2602.21913