import math
import random
import statistics
import pandas
import matplotlib.pyplot as plt


def prime(n, i=2):
    if n == i:
        return True
    if n > 2:
        if n % i == 0:
            return False
        else:
            return prime(n, i + 1)
    else:
        return False


print("Test prime dla 7, 14 i 13:", prime(7), prime(14), prime(13))


def select_primes(x):
    result = []
    for number in x:
        if prime(number):
            result.append(number)
    return result


print("Test select_primes dla [2,3,7,8,9,13,25,29]", select_primes([2,3,7,8,9,13,25,29]))

# Zad. 2

vector_one = [3, 8, 9, 10, 12]
vector_two = [8, 7, 7, 5, 6]

suma = []
iloczyn = []

for i in range(len(vector_one)):
    suma.append(vector_one[i] + vector_two[i])
    iloczyn.append(vector_one[i] * vector_two[i])

print("suma", suma, "iloczyn", iloczyn)

skalar = 0

for i in range(len(vector_one)):
    skalar += vector_one[i] * vector_two[i]

print("Iloczyn skalarny:", skalar)


def vector_len(v):
    result = 0
    for j in v:
        result += j**2
    return math.sqrt(result)

print("Długośc wektorów")
print(vector_len(vector_one))
print(vector_len(vector_two))

vector_random = [7, 68, 73, 20, 16, 39, 37, 62, 78, 36, 19, 37, 68, 12, 49, 95, 40, 48, 25, 75, 33, 80, 85, 40, 67, 96,
                 87, 67, 71, 47, 2, 21, 37, 24, 45, 11, 67, 60, 41, 5, 40, 57, 10, 54, 59, 7, 55, 7, 75, 18]

# można w sumie min(vector_one)
min = vector_random[0]
max = vector_random[0]


for ranint in vector_random:
    if ranint < min:
        min = ranint
    if ranint > max:
        max = ranint

print("Max:", max, "Min:", min)

deriviate = statistics.stdev(vector_random)
print("Deriviate", deriviate)


def normilize(vector):
    new_vector = []
    for x in vector:
        new_vector.append((x - min) / (max - min))
    return new_vector


normilized_vector = normilize(vector_random)
print("Normalizacja", normilized_vector)

index_of_max = 0
for i in range(len(vector_random)):
    if vector_random[i] == max:
        index_of_max = i

print("Orginalne max:", max, "Index max:", index_of_max, "Nowa wartość:", normilized_vector[index_of_max])


def standardize(vector):
    new_vector = []
    mean_of_vector = statistics.mean(vector)
    for i in vector:
        new_vector.append((i - mean_of_vector) / deriviate)
    return new_vector


standarized_vector = standardize(vector_random)
print("Standaryzacja", standarized_vector)

print("Nowe odchylenie:", statistics.stdev(standarized_vector), "Nowa średia:", statistics.mean(standarized_vector))


def dyskretyzacja(vector):
    result = []
    for i in vector:
        acc = 0
        while i > 10:
            acc += 10
            i -= 10
        result.append((acc, acc+10))
    return result


descretisized_vector = dyskretyzacja(vector_random)

print("Dyskretyzacja", descretisized_vector)

# Zad. 3

miasta = pandas.read_csv("miasta.csv")

print("Dane tabela:", miasta.values)


data_to_add = pandas.DataFrame({
    "Rok": 2010,
    "Gdansk": 460,
    "Poznan": 555,
    "Szczecin": 405
}, index=[len(miasta)])

miasta = miasta.append(data_to_add, ignore_index=True)

plt.plot(miasta["Rok"], miasta["Gdansk"], color='red', linewidth=2, marker='o')
plt.xlabel("Rok")
plt.ylabel("Gdansk mieszkancy")
plt.show()

plt.plot(miasta["Rok"], miasta["Gdansk"], color='red', linewidth=2, marker='o', label='Gdansk')
plt.plot(miasta["Rok"], miasta["Szczecin"], color='green', linewidth=2, marker='o', label='Szczecin')
plt.plot(miasta["Rok"], miasta["Poznan"], color='blue', linewidth=2, marker='o', label='Poznan')
plt.legend()
plt.show()

