import pygad
import numpy
import time

Lab = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#Oceniamy odległość od wyjścia !!!!!!!
#Wykonuje po kolei ruchy z solution
#Na końcu jesteśmy we współrzędnych (x, y)
#Zwróć odległość od końca np. -(|x - x.end| + |y - y.end|)

gene_space = [0, 1, 2, 3]
desired_fitness = 0

#Taktyki na uderzenia w ścianę
#nr.1 Śmierć, uderzenie w ścianę kończy symulację i miejsce kolizjii to (x, y)
#ostra ocena wolna ewolucja, ale ma czyste rozwiązania
#nr.2 odbicie, ignorujemy wejście w ścianę, ruch pomijamy i bierzemy kolejny
#ruchy zostaną wykorzystane do końca i zwracamy miejsce zatrzymania
# rozwiązanie będzie miało brudne rucchy "w ścienę" mozna naprawic post proccesingiem
def fitness_func(solution, solution_idx):
    pos = (1, 1)
    end_pos = (10, 10)
    for gene in solution:
        if gene == 0:
            "prawo"
        if gene == 1:
            "lewo"
        if gene == 2:
            "góra"
        if gene == 3:
            "dół"
    return fitness


fitness_function = fitness_func

#ile chromsomĂłw w populacji
#ile genow ma chromosom
sol_per_pop = 10
num_genes = 30

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 30
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 5

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty


ga_instance = pygad.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           stop_criteria=["reach_0"],
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes)
ga_instance.run()




