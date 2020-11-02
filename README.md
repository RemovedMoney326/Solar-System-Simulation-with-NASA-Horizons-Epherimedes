# N-Body Simulation using NASA Horizons Data
Jupyter Notebook using a differential equation integration solver based on a Leapfrog Algorithm and vectorized ODEs to simulate and plot the orbits from different objects in the solar system with initial position and velocity vectors provided by the JPL Horizons System by NASA .
# Abstract
The goal of this Jupyter Notebook is to make an interactive ipython notebook available,
with which one can simulate and produce 3D plots for the orbits of any object within the solar
system during a settable simulation time tmax and timestep ∆t. This is achieved through computation
of an N-Body simulation for the 10 main bodies within the solar systems frame of reference
(the Sun, the 8 planets and the dwarf planet Pluto) using accurate initial position and velocity
vector data provided by the NASA Horizons System, with the possibility of adding any number of extra
N-Bodies to the simulation through the epherimedes provided by the same system (as long as
their id/target_name and mass are known).
