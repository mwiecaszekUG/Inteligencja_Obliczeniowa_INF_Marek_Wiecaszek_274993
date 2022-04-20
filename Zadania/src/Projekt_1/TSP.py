import numpy
import matplotlib.pyplot as plt
import pygad
import random


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
            if con.connects[0] == self and con.connects[1] == other_city or\
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

        number_of_routes = number_of_cities * 1.5 + 5
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
            if not city.connections:
                bad_connections = True
                c, r = make_cons()
                print("Remaking the list")
                break

    return c, r


number_of_cities = int(input('Number of cities to test = '))

cities_1, routes_1 = make_map()

# shows all connections
for r in routes_1:
    r.show_route()

aaa = []
for c in cities_1:
    aaa.append(c.name)
print(aaa)
# shows indexes of cities connected with the city
# print(cities_1[0].connected_with_indexes(cities_1))

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
                # print("dodaje miasto nr", len(cities_visited))
                cities_visited.append(int(move))
        else:
            fitness += 1000

    if len(cities_visited) == number_of_cities:
        fitness = fitness / 3

    return -int(fitness)


fitness_function = fitness_func

gene_space = list(range(0, number_of_cities))

sol_per_pop = 1000
num_genes = number_of_cities * 3

num_parents_mating = 400
num_generations = 100
keep_parents = 200

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 20

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


solution, solution_fitness, solution_idx = ga_instance.best_solution()
print(solution)
ga_instance.plot_fitness()


# napisz funkcje clean_up(result)
