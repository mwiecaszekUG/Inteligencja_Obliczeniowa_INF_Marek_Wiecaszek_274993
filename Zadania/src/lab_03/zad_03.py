import pygad
import numpy
import time
import math


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


#funkcja czyszcząca wynik z niepotrzebnych ruchów
def result_cleanup(solution):
    result = []
    pos = (1, 1)
    for i in range(len(solution)):
        if solution[i] == 0:
            if Lab[pos[0]][pos[1] + 1] == 0:
                pos = (pos[0], pos[1] + 1)
                result.append("prawo")
        if solution[i] == 1:
            if Lab[pos[0]][pos[1] - 1] == 0:
                pos = (pos[0], pos[1] - 1)
                result.append("lewo")
        if solution[i] == 2:
            if Lab[pos[0] - 1][pos[1]] == 0:
                pos = (pos[0] - 1, pos[1])
                result.append("góra")
        if solution[i] == 3:
            if Lab[pos[0] + 1][pos[1]] == 0:
                pos = (pos[0] + 1, pos[1])
                result.append("dół")
        if pos == (10, 10):
            fitness = 0
            print("Ilość ruchów: ", len(result))
            print("Wynik: ", result)
            return fitness



gene_space = [0, 1, 2, 3]
desired_fitness = 0

#Taktyki na uderzenia w ścianę
#nr.1 Śmierć, uderzenie w ścianę kończy symulację i miejsce kolizjii to (x, y)
#ostra ocena wolna ewolucja, ale ma czyste rozwiązania
#nr.2 odbicie, ignorujemy wejście w ścianę, ruch pomijamy i bierzemy kolejny
#ruchy zostaną wykorzystane do końca i zwracamy miejsce zatrzymania
# rozwiązanie będzie miało brudne rucchy "w ścienę" mozna naprawic post proccesingiem
#Oceniamy odległość od wyjścia !!!!!!!
#Wykonuje po kolei ruchy z solution
#Na końcu jesteśmy we współrzędnych (x, y)
#Zwróć odległość od końca np. -(|x - x.end| + |y - y.end|)

# 0=prawo 1=lewo 2=góra 3=dół

#Wersja pobłażliwa (z reguły znajduję rozwiązanie w 500 generacjach)
#dodatkowo rozwiązania mają w sobie dużo niepotrzebnych ruchów (wchodzenie w ściany),
#ale stosunkowo mało "chodzeniaw miejscu"


def fitness_func(solution, solution_idx):
    pos = (1, 1)
    end_pos = (10, 10)
    for i in range(len(solution)):
        if solution[i] == 0:
            if Lab[pos[0]][pos[1]+1] == 0:
                pos = (pos[0], pos[1] + 1)
        if solution[i] == 1:
            if Lab[pos[0]][pos[1]-1] == 0:
                pos = (pos[0], pos[1] - 1)
        if solution[i] == 2:
            if Lab[pos[0]-1][pos[1]] == 0:
                pos = (pos[0]-1, pos[1])
        if solution[i] == 3:
            if Lab[pos[0]+1][pos[1]] == 0:
                pos = (pos[0]+1, pos[1])
        if pos == end_pos:
            return result_cleanup(solution)
    fitness = -(math.fabs(pos[0] - end_pos[0]) + math.fabs(pos[1] - end_pos[1]))
    return fitness


#Wersja rygorystyczna (kary za wchodzenie w ścianę)
#Rozwiązania dalej zawierają wejścia w ścianę dodatkowo pojawija się chodzenie w kółko,
#Dodatkowo znalezienie rozwiązania wymaga zdecydowanie większej ilości pokoloń niż rozwiązanie pobłażliwe
#Pierwsze znalezione rozwiązanie tym sposobem oceny nastąpiło po 23462 generacji i zajęło 16 sekund

# def fitness_func(solution, solution_idx):
#     pos = (1, 1)
#     end_pos = (10, 10)
#     colisions = 0
#     for i in range(len(solution)):
#         if solution[i] == 0:
#             if Lab[pos[0]][pos[1]+1] == 0:
#                 pos = (pos[0], pos[1] + 1)
#             else:
#                 colisions += 1
#         if solution[i] == 1:
#             if Lab[pos[0]][pos[1]-1] == 0:
#                 pos = (pos[0], pos[1] - 1)
#             else:
#                 colisions += 1
#         if solution[i] == 2:
#             if Lab[pos[0]-1][pos[1]] == 0:
#                 pos = (pos[0]-1, pos[1])
#             else:
#                 colisions += 1
#         if solution[i] == 3:
#             if Lab[pos[0]+1][pos[1]] == 0:
#                 pos = (pos[0]+1, pos[1])
#             else:
#                 colisions += 1
#         if pos == end_pos:
#             return result_cleanup(solution)
#     fitness = -(math.fabs(pos[0] - end_pos[0]) + math.fabs(pos[1] - end_pos[1]))*((colisions+1)**2)
#     return fitness


fitness_function = fitness_func

sol_per_pop = 10
num_genes = 30

num_parents_mating = 5
# num_generations = 500
# wymagane dla algorytmu rygorystycznego
num_generations = 100000
keep_parents = 2

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 7

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

print("Ostateczny wynik został pozbawiony ruchów w ściany")
start = time.time()
ga_instance.run()
stop = time.time()
print("czas operacji: ", stop-start)
print("ilość generacji: ", ga_instance.generations_completed)
print("ocena wyniku: ", ga_instance.best_solutions_fitness[-1])







