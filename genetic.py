#Gentic Aproach

import numpy as np


matrix_A = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

def initial_population(population_size, array_size):
    return [np.random.randint(0,2,array_size) for _ in range(population_size)]

def calc_fitness(subarray, matrix):
    return np.sum(subarray * matrix)

def mutate(subarray):
    mutation_point = np.random.randint(len(subarray))
    subarray [mutation_point] = 1 - subarray[mutation_point]
    return subarray



def crossover(parent1, parent2) :
  crossover_point = np.random.randint(len(parent1))
  child = np.concatenate((parent1[: crossover_point], parent2[crossover_point:]))
  return child

def genatic_max_subarry_sum(matrix, population_size, generations):
    rows, cols = len(matrix), len(matrix[0])
    population = initial_population(population_size, cols)

    for generation in range(generations):
        fitness_scores = [calc_fitness(candidate, matrix) for candidate in population]
        best_candidate = population[np.argmax(fitness_scores)]

        if np.max(fitness_scores) == np.sum(np.abs(matrix)):
         break

         new_pop = [best_candidate]

         for _ in range(population_size - 1) :
          parent1 = population[np.random.choice(range(population_size))]
          parent2 = population[np.random.choice(range(population_size))]
          child = crossover(parent1, parent2)

          if np.random.rand() < 0.1 :
             child = mutate(child)
          new_pop.append(child)

         population= new_pop

    best_solution = population[np.argmax([calc_fitness(candidate, matrix) for candidate in population])]

    return best_solution, calc_fitness(best_solution,matrix)

best_subarray, max_subarry_sum = genatic_max_subarry_sum(matrix_A, population_size=10, generations= 100)

print("best subarry (1: include, 0: exclude)", best_subarray)
print("max sub array sum:", max_subarry_sum)
