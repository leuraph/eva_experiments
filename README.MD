# Summary

This repository holds the numerical experiments
performed in [1].
The underlying boundary value problem is
$$
-\text{div} (\mathbf A(x) \nabla u(x))
+ \phi(u)
=
f
$$
with homogeneous Dirichlet boundary conditions.
As in the paper, experiments are divided into linear and
nonlinear experiments corresponding to either
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