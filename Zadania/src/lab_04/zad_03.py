import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt


# Set-up hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

# Call instance of GlobalBestPSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2,
                                    options=options)

# Perform optimization
stats = optimizer.optimize(fx.levi, iters=100)
stats2 = optimizer.optimize(fx.crossintray, iters=100)
stats3 = optimizer.optimize(fx.eggholder, iters=100)

cost_history = optimizer.cost_history

# na wykresie wyniki dla poszczególnych funkcji zaczynają się od 0, 100, 200
plot_cost_history(cost_history)
plt.show()
