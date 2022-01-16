# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: January 17, 2022
#
#
# You can solve the exercises below by using standard Python 3.9 libraries, NumPy, Matplotlib, Pandas, PyMC3.
# You can browse the documentation: [Python](https://docs.python.org/3.9/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/3.3.1/contents.html), [Pandas](https://pandas.pydata.org/pandas-docs/version/1.2.5/), [PyMC3](https://docs.pymc.io/).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2021/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others.** 
#

# %matplotlib inline
import numpy as np   # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc3 as pm   # type: ignore

# ### Exercise 1 (max 3 points)
#
# The file [birds_romania.csv](birds_romania.csv) contains data about birds recording collected in Romania (source: https://xeno-canto.org). Read them in a `DataFrame`, be sure the columns with latitude (`lat`), longitude (`lng`), and altitude (`alt`) are called `latitude`, `longitude`, and `altitude`. 

pass

# ### Exercise 2 (max 3 points)
#
#
# Plot a histogram of altitudes: draw a bar for each 100m interval.

pass

# ### Exercise 3 (max 6 points)
#
# In order to compute the distance between two points on Earth, given in terms of latitude and longitude, one can use the easier formula valid for spheres. If $R$ is the radius, $\phi$ is the latitude, $\lambda$ the longitude, and $\Delta$ denotes the difference between the coordinates of the two points: 
#
# \begin{align}
#   d &= 2\cdot R\cdot\arcsin \sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \left(1 - \sin^2\left(\frac{\Delta\phi}{2}\right) - \sin^2\left(\frac{\phi_1 + \phi_2}{2}\right)\right)\cdot\sin^2\left(\frac{\Delta\lambda}{2}\right)}.
# \end{align}
#
# By default use the mean Earth's radius of 6371.009km. For example, The distance between $(45.1^\circ, 9.2^\circ)$ (near Pavia) and $(45.3^\circ, 9.4^\circ)$ (near Lodi) should be approximately 27.2km (since the Earth is not a sphere, the given formula has an error up to 0.5%).
#
#
# Write a function `earth_dist` to compute this distance. To get the full marks, you should declare correctly the type hints (the signature of the function) and add a doctest string.
#
#

pass

# ### Exercise 4 (max 4 points)
#
# Each record has a recorder name (column `rec`) and the time and date of collection. Create a new column `timestamp` to make easier sorting the data chronologically. Hint: pandas has `datetime` objects. 

pass

# ### Exercise 5 (max 7 points)
#
# Consider the recorder "Marco Dragonetti": take his records in chronological order and compute the total distance among them: assume this is the distance Marco has travelled for recording bird songs. If Marco had 3 records $a$, $b$, $c$, the total distance would be the distance between $a$ and $b$ plus the distance between $b$ and $c$. 
#

pass

# ### Exercise 6 (max 4 points)
#
# Compute the median of the total distances travelled by all the recorders.  

pass

# ### Exercise 7 (max 2 points)
#
# Count the number of records in which a bird has been seen (column `bird-seen`) and the number of records in which a bird has not been seen.

pass

# ### Exercise 8 (max 4 points)
#
# Consider this statistical model: if the probability of seeing a bird is $p$, the total number of birds seen should have a [binomial](https://docs.pymc.io/en/v3/api/distributions/discrete.html#pymc3.distributions.discrete.Binomial) distribution. Your *a priori* estimation of $p$ is uniform over the whole interval from 0 to 1. Use PyMC to sample the posterior distributions after having observed the actual values of birds seen (computed in the previous exercise).  Plot the results.

pass
