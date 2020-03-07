# Vortex Panel Method

Pythonic Vortex Panel Method implementation via GMRES solver.

Obtain the solution of pressure and velocity distributions across an airfoil.

See the [Panel Method notebook for the lean implementation](https://github.com/KikeM/vortex-method/blob/master/src/0-Panel-Method.ipynb), the [Geometry notebook](https://github.com/KikeM/vortex-method/blob/master/src/1-Geometry.ipynb) for the construction of the arrays and the [Solver notebook](https://github.com/KikeM/vortex-method/blob/master/src/2-Solver.ipynb) for the construction of the numerical solver. 

The code has been implemented with a half-way Object-Oriented approach via the use of Jupyter notebooks. In this way, the user can follow the implementation with the markdown explanations and yet use it to do parameter sweeps via the `%run` magic command (see [Panel effects notebook](https://github.com/KikeM/vortex-method/blob/master/src/6-Panel-Effect.ipynb) for an example of this approach). 
