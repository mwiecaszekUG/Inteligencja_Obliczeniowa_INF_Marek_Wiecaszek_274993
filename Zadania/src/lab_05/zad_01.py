import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np
import math
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt


def endurance(args):
    return math.exp(-2*(args[1]-math.sin(args[0]))**2)+math.sin(args[2]*args[3])+math.cos(args[4]*args[5])


def optimize_func(swarm_entities):
    # result = []
    # for instance in swarm_entities:
    #     result.append(-endurance(instance))
    # return result
    n_particles = swarm_entities.shape[0]
    j = [-endurance(swarm_entities[i]) for i in range(n_particles)]
    return np.array(j)


x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6,
                                    options=options, bounds=my_bounds)
optimizer.optimize(optimize_func, iters=1000)
cost_history = optimizer.cost_history

cost_history = np.negative(cost_history)

plot_cost_history(cost_history)
plt.show()

