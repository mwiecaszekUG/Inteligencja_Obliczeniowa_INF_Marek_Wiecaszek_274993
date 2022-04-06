import numpy
import pyswarms as ps
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_cost_history


S = [1, 2, 3, 6, 10, 17, 25, 29, 30, 41, 51, 60, 70, 79, 80]


def fitness_func(solution):
    sum1 = numpy.sum(solution * S)
    solution_invert = 1 - solution
    sum2 = numpy.sum(solution_invert * S)
    fitness = numpy.abs(sum1-sum2)
    return fitness


def optimize_func(swarm_entities):
    n_particles = swarm_entities.shape[0]
    j = [fitness_func(swarm_entities[i]) for i in range(n_particles)]
    return numpy.array(j)


options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 2, 'p': 1}

optimizer = ps.discrete.BinaryPSO(n_particles=10, dimensions=15,
options=options)
_, pos = optimizer.optimize(optimize_func, iters=30, verbose=True)
cost_history = optimizer.cost_history\

plot_cost_history(cost_history)
plt.show()
