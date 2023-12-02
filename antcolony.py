import numpy as np
import random

def update_pheromones(pheromone_list, ant_row, ant_column,evap_coefficient, ant_pheromone):
  pheromone_list[ant_row][ant_column] = (1 - evap_coefficient) * pheromone_list[ant_row][ant_column] + ant_pheromone


def get_ant_valid_position(ant_row, ant_column, matrix):
    valid_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Creating a list of valid neighbors
    valid_neighbors = [(ant_row + i, ant_column + j) for i, j in valid_directions if 0 <= ant_row + i < len(matrix) and 0 <= ant_column + j < len(matrix[0])]

    if valid_neighbors:
        return random.choice(valid_neighbors)
    # If there are no valid positions, then return current position
    else:
        return ant_row, ant_column


def move_ant(ant, pheromones, matrix) :
  ant_row = ant[0]
  ant_column = ant[1]
  new_ant_row = 0
  new_ant_column = 0

  rows, columns = len(matrix), len(matrix[0])

  #If the ant is in the first row, it can only go right or down
  if ant_row == 0 :

    #If the pheromone is bigger for the right neigbhour, move the ant right
    if ant_column +1 < columns and (pheromones[ant_row][ant_column+1] > pheromones[ant_row+1][ant_column] or matrix[ant_row][ant_column+1] > matrix[ant_row+1][ant_column]):
      new_ant_row = ant_row
      new_ant_column = ant_column +1

    #If the pheromone is bigger for the down neigbhour, move the ant down
    elif ant_row +1< rows and ant_column < columns-1 :
      if pheromones[ant_row +1][ant_column] > pheromones[ant_row][ant_column +1] or matrix[ant_row +1][ant_column] > matrix[ant_row][ant_column +1]:
        new_ant_row,new_ant_column = ant_row+1,ant_column

    #Move ant randomly (down or right) if pheromones are equivalent
    else :
      new_ant_row, new_ant_column = get_ant_valid_position(ant_row, ant_column, matrix)
  #If the ant is in the last row, it can only move up or right
  elif ant_row == len(matrix) - 1:

    if ant_column +1 < columns and (pheromones[ant_row][ant_column + 1] > pheromones[ant_row - 1][ant_column] or matrix[ant_row][ant_column + 1] > matrix[ant_row - 1][ant_column] ):
      # Move the ant right
      new_ant_row, new_ant_column = ant_row, ant_column + 1

    # Move the ant up
    elif ant_row > 0 and ant_column < columns - 1:
      if pheromones[ant_row - 1][ant_column] > pheromones[ant_row][ant_column] or matrix[ant_row - 1][ant_column] > matrix[ant_row][ant_column]:
        new_ant_row, new_ant_column = ant_row - 1, ant_column

    # Randomly move ant if pheromones are equal
    else:
        new_ant_row, new_ant_column = get_ant_valid_position(ant_row, ant_column, matrix)

  # If the ant is in the middle of the matrix
  else:
        # Move the ant right
        if ant_column < len(matrix[0]) - 1 and (pheromones[ant_row][ant_column + 1] > pheromones[ant_row][ant_column - 1] or matrix[ant_row][ant_column + 1] > matrix[ant_row][ant_column - 1]):
            new_ant_row, new_ant_column = ant_row, ant_column + 1
        # Move the ant left
        elif ant_column > 0 and (pheromones[ant_row][ant_column - 1] > pheromones[ant_row][ant_column] or matrix[ant_row][ant_column - 1] > matrix[ant_row][ant_column]):
            new_ant_row, new_ant_column = ant_row, ant_column - 1
        # Move the ant down
        elif ant_row < len(matrix) - 1 and (pheromones[ant_row + 1][ant_column] > pheromones[ant_row - 1][ant_column] or matrix[ant_row + 1][ant_column] > matrix[ant_row - 1][ant_column]):
            new_ant_row, new_ant_column = ant_row + 1, ant_column
        # Move the ant up
        elif ant_row > 0 and pheromones[ant_row - 1][ant_column] > (pheromones[ant_row + 1][ant_column] or matrix[ant_row - 1][ant_column] > matrix[ant_row + 1][ant_column]):
            new_ant_row, new_ant_column = ant_row - 1, ant_column
        else:
            #Move the ant randomly
            new_ant_row, new_ant_column = get_ant_valid_position(ant_row, ant_column, matrix)
  return new_ant_row, new_ant_column

#Initializations
num_ants = 30
num_coordinates = 2
num_iterations = 400
#ACO parameters
evap = 0.8
ant_pheromone = 0.4
initial_phero_value = 0.3

def ACO(num_ants,num_coordinates,num_iterations,evap,ant_pheromone,matrix):
  #List of ants
  ants = [] 
  #Matrix in which there will be the indexes
  submatrix_frequency = {}
  #Creating a matrix of random pheromones, a pheromone is associated to each value of the matrix
  pheromone_matrix = np.full_like(matrix,np.random.rand(),dtype="float")
  print(pheromone_matrix.shape)
  #Putting an ant on each element of the matrix
  for i in range(num_ants):
    ant_row = i // matrix_columns
    ant_column = i % matrix_columns
    ants.append([ant_row % matrix_rows, ant_column])
  
  for ant in ants:
    ant_row_initial, ant_column_initial = ant

  for i in range (num_iterations):
    for ant in ants:
      ant_row_initial, ant_column_initial = ant

      # Updating ant postition
      ant_row_updated, ant_column_updated = move_ant(ant, pheromone_matrix, matrix)
      # Using new ant position to update pheromones
      update_pheromones(pheromone_matrix, ant_row_updated, ant_column_updated, evap, ant_pheromone)

      # Updating position in the list of ant
      ant[0] = ant_row_updated
      ant[1] = ant_column_updated
      current_submatrix = (min(ant_row_initial, ant_row_updated), max(ant_row_initial, ant_row_updated),
                             min(ant_column_initial, ant_column_updated), max(ant_column_initial, ant_column_updated))
      #current_submatrix = (ant_row_initial, ant_row_updated, ant_column_initial, ant_column_updated)
      submatrix_frequency[current_submatrix] = submatrix_frequency.get(current_submatrix, 0) + 1
  median_submatrix = np.median(list(submatrix_frequency.keys()), axis=0)
  median_submatrix = tuple(map(int, median_submatrix))
  # Getting the indexes of the sub-matrix
  i1, i2, j1, j2 = median_submatrix
  print("Les fourmis ont le plus circulé dans la sous-matrice aux indices (i1, i2, j1, j2):", i1, i2, j1, j2)
  # Printing maximum sum sub-matrix
  matrix_np = np.array(matrix)
  submatrix = matrix_np[i1:i2 + 1, j1:j2 + 1]
  print("La sous-matrice la plus visitée par les fourmis est :")
  print(submatrix, end="\n")

matrix = [[1, 2, -1, -4, -20],
          [-8, -3, 4, 2, 1],
          [3, 8, 10, 1, 3],
          [-4, -1, 1, 7, -6]]

ACO(30,2,400,0.8,0.4,matrix)

