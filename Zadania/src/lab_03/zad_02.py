# 𝑒𝑛𝑑𝑢𝑟𝑎𝑛𝑐𝑒(𝑥, 𝑦, 𝑧, 𝑣, 𝑢, 𝑤) = 𝑒−2∙(𝑦−sin (𝑥))2 + sin(𝑧 ∙ 𝑢) + cos (𝑣 ∙ 𝑤)
import pygad
import numpy
import random
import math


def endurence(x, y, z, v, u, w):
    return math.e ** (-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)


S = []
for i in range(6):
    S.append(random.uniform(0, 1))
#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1

gene_space = {'low': 0,
              'high': 1}


#definiujemy funkcjÄ fitness
def fitness_func(solution, solution_idx):
    fitness = endurence(solution[0], solution[1], solution[2], solution[3], solution[4], solution[5])
    return fitness


fitness_function = fitness_func

#ile chromsomĂłw w populacji
#ile genow ma chromosom
sol_per_pop = 10
num_genes = len(S)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 1000
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 25

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w

ga_instance = pygad.GA(gene_space=gene_space,
                            num_generations=num_generations,
                            num_parents_mating=num_parents_mating,
                            fitness_func=fitness_function,
                            sol_per_pop=sol_per_pop,
                            num_genes=num_genes,
                            parent_selection_type=parent_selection_type,
                            keep_parents=keep_parents,
                            crossover_type=crossover_type,
                            mutation_type=mutation_type,
                            mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

print(ga_instance.best_solutions_fitness[-1])
ga_instance.plot_fitness()