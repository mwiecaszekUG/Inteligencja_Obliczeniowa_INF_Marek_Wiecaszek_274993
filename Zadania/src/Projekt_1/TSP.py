import numpy
import pyswarms as ps
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_cost_history
import random


class City:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, neighbour,  route):
        self.connections.append(route)
        neighbour.connections.append(route)

    def delete_connection(self, route):
        self.connections.remove(route)


class Route:
    def __init__(self, name, cost):
        self.cost = cost
        self.name = name

    def change_cost(self, new_cost):
        self.cost = new_cost


number_of_cities = int(input('Number of cities to test = '))
city_list = []

file = open("cities.txt", "r")
names = []

for i in file:
    names.append(i.split(",")[0])

for i in range(number_of_cities):
    city_list.append(City(names[random.randint(0, len(names) - 1)], []))

for town in city_list:
    print(town.name)

number_of_routes = number_of_cities*3
max_cost = 250

for i in range(number_of_routes):
    con = Route(random.randint(0, len(names) - 1), random.randint(0, max_cost))
    city_list[random.randint(0, number_of_cities - 1)].add_connection(city_list[random.randint(0, number_of_cities)], con)



