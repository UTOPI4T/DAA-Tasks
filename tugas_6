# Pertemuan 6 #

import matplotlib
import matplotlib.pyplot as plt
import random
import time
import itertools

def exact_TSP(cities):
  return shortest(alltours(cities))

def shortest(tours):
  return min(tours, key=total_distance)

alltours = itertools.permutations

cities = (1,2,3)

list(alltours(cities))

def total_distance(tour):
  return sum(distance(tour[i],tour[i-1]) for i in range(len(tour)))

City = complex
def distance(A, B):
  return abs(A-B)

A = City(300,0)
B = City(0,400)
distance(A,B)

tour = exact_TSP(cities8)

print(tour)
print(total_distance(tour))

def Cities(n):
  return set(City(random.randrange(10,890), random.randrange(10,590)) for c in range(n))

random.seed('seed')
cities8, cities10, cities100, cities1000= Cities(8), Cities(10), Cities(100), Cities(1000)
cities8

import time
def plot_tour(algorithm, cities):
  t0 = time.time()
  tour = algorithm(cities)
  t1 = time.time()
  plotline(list(tour) + [tour[0]])
  plotline([tour[0]], 'rs')
  plt.show()
  print("{} citiy tour; total distance = {:.1f}, time = {:.3f} secs for{}".format(len (tour), total_distance(tour), t1-t0, algorithm.__name__))

def plotline(points, style='bo-'):
  X, Y = XY(points)
  plt.plot(X, Y, style)

def XY(points):
  return[p.real for p in points], [p.imag for p in points]

plot_tour(exact_TSP, cities8)
plot_tour(exact_TSP,cities10)


