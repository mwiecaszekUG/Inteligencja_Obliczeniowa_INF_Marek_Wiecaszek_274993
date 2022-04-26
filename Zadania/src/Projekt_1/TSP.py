import numpy
import matplotlib.pyplot as plt
import pygad
import random
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history
import time


class City:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, neighbour, route):
        self.connections.append(route)
        neighbour.connections.append(route)

    def delete_connection(self, route):
        self.connections.remove(route)

    def connected_with_indexes(self, l):
        result = []
        for con in self.connections:
            if con.connects[0] != self:
                result.append(l.index(con.connects[0]))
            else:
                result.append(l.index(con.connects[1]))
        return result

    def find_connection_with(self, other_city):
        for con in self.connections:
            if con.connects[0] == self and con.connects[1] == other_city or \
                    con.connects[1] == self and con.connects[0] == other_city:
                return con


class Route:
    def __init__(self, name, cost, connects):
        self.cost = cost
        self.name = name
        self.connects = connects

    def change_cost(self, new_cost):
        self.cost = new_cost

    def show_route(self):
        print(self.connects[0].name, "---", self.cost, "---", self.connects[1].name)


def make_map():
    def check_duplicate(c1, c2, routes):
        if c1 == c2:
            return False
        for r in routes:
            if r.connects[0] == c1 and r.connects[1] == c2 or r.connects[0] == c2 and r.connects[1] == c1:
                return False
        return True

    def make_cons():
        city_list = []
        file = open("cities.txt", "r")
        names = []
        for i in file:
            names.append(i.split(",")[0])
        for i in range(number_of_cities):
            city_list.append(City(names[random.randint(0, len(names) - 1)], []))
        number_of_routes = number_of_cities * 3
        max_cost = 250
        route_list = []
        i = 0
        while i < number_of_routes:
            city_1 = city_list[random.randint(0, number_of_cities - 1)]
            city_2 = city_list[random.randint(0, number_of_cities - 1)]
            if check_duplicate(city_1, city_2, route_list):
                con = Route(random.randint(0, len(names) - 1), random.randint(5, max_cost), [city_1, city_2])
                route_list.append(con)
                city_1.add_connection(city_2, con)
                i += 1
        return city_list, route_list
    bad_connections = True
    c, r = make_cons()
    while bad_connections:
        bad_connections = False
        for city in c:
            if len(city.connections) < 2:
                bad_connections = True
                c, r = make_cons()
                print("Remaking the list")
                break
    return c, r


number_of_cities = int(input('Number of cities to test = '))

cities_1, routes_1 = make_map()

# shows all connections
# print("All possible connections: ")
# for r in routes_1:
#     r.show_route()
#
# aaa = []
# for c in cities_1:
#     aaa.append(c.name)
# print("\nList of all cities: ")
# print(aaa)
# # shows indexes of cities connected with the city
# for c in cities_1:
#     print(c.connected_with_indexes(cities_1))

starting_point = 0


def fitness_func(solution, solution_idx):
    cities_visited = [starting_point]
    previous_city = cities_1[starting_point]
    fitness = 0
    for move in solution:
        legal_moves = previous_city.connected_with_indexes(cities_1)
        if int(move) in legal_moves:
            con = cities_1[int(move)].find_connection_with(previous_city)
            fitness += con.cost
            previous_city = cities_1[int(move)]
            if int(move) not in cities_visited:
                cities_visited.append(int(move))
        else:
            fitness += 1000

    if len(cities_visited) == number_of_cities:
        fitness = fitness / 3
    return -int(fitness)

def fitness_func_swarm(solution):
    cities_visited = [starting_point]
    previous_city = cities_1[starting_point]
    fitness = 0
    for i in range(number_of_cities * 2):
        move = solution[i]
        legal_moves = previous_city.connected_with_indexes(cities_1)
        if int(move) in legal_moves:
            con = cities_1[int(move)].find_connection_with(previous_city)
            fitness += con.cost
            previous_city = cities_1[int(move)]
            if int(move) not in cities_visited:
                cities_visited.append(int(move))
        else:
            fitness += 1000

    if len(cities_visited) == number_of_cities:
        fitness = fitness / 3
    return int(fitness)

def fitness_func_big(solution, solution_idx):
    cities_visited = [starting_point]
    previous_city = cities_1[starting_point]
    fitness = 0
    for move in solution:
        legal_moves = previous_city.connected_with_indexes(cities_1)
        if int(move) in legal_moves:
            con = cities_1[int(move)].find_connection_with(previous_city)
            fitness += con.cost
            previous_city = cities_1[int(move)]
            if int(move) not in cities_visited:
                cities_visited.append(int(move))
        else:
            fitness += 1000
    if len(cities_visited) == number_of_cities:
        fitness = fitness / 3
    return -int(fitness)*(number_of_cities/len(cities_visited)*5)


def swarm_func(swarm_entities):
    n_particles = swarm_entities.shape[0]
    j = [fitness_func_swarm(swarm_entities[i]) for i in range(n_particles)]
    return numpy.array(j)


def solution_cleanup(solution):
    real_weight = 0
    moves_used = [0]
    cities_visited = [starting_point]
    previous_city = cities_1[starting_point]
    two_back = cities_1[starting_point]
    for move in solution:
        if len(cities_visited) == number_of_cities:
            print("Odwiedzono wszystkie miasta")
            return real_weight, moves_used
        legal_moves = previous_city.connected_with_indexes(cities_1)
        if int(move) in legal_moves:
            moves_used.append(int(move))
            con = cities_1[int(move)].find_connection_with(previous_city)
            if two_back != cities_1[int(move)]:
                real_weight += con.cost
            two_back = previous_city
            previous_city = cities_1[int(move)]
            if int(move) not in cities_visited:
                cities_visited.append(int(move))
        else:
            print("Znalezione nielegalny ruch (poleciał samolotem)")
    print("Odwiedzone miasta: ", len(cities_visited))
    return real_weight, moves_used


fitness_function = fitness_func_big

gene_space = list(range(0, number_of_cities))

sol_per_pop = 500
num_genes = number_of_cities * 5

num_parents_mating = 150
num_generations = 100
keep_parents = 100

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 100 / number_of_cities + 1

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

print("zaczynam")
gen_start = time.time()
ga_instance.run()
gen_stop = time.time()
print("skonczyłem")

solution, solution_fitness, solution_idx = ga_instance.best_solution()

ga_instance.plot_fitness()

print("Cost of fitness genetic: ", solution_fitness)

cost, route_taken = solution_cleanup(solution)

print("Route taken genetic", route_taken)
print("Cost of the route taken genetic: ", cost)
print("Time of operation: ", gen_stop- gen_start)




# options = {'c1': 0.3, 'c2': 0.5, 'w': 0.9, 'k': 25, 'p': 1}
#
# x_max = numpy.ones(number_of_cities * 2) * (number_of_cities - 1)
# x_min = numpy.zeros(number_of_cities * 2)
# my_bounds = (x_min, x_max)
#
# optimizer = ps.single.GlobalBestPSO(n_particles=3000, dimensions=number_of_cities * 2,
#                                     options=options, bounds=my_bounds)
# swarm_start = time.time()
# _, pos = optimizer.optimize(swarm_func, iters=100, verbose=True)
# cost_history = optimizer.cost_history
# swarm_stop = time.time()
#
# cost_history = numpy.negative(cost_history)
# cost, route_taken = solution_cleanup(pos)
# print(cost)
# print(route_taken)
# plot_cost_history(cost_history)
# plt.show()
#
# print("Time of swarm: ", swarm_stop-swarm_start)
