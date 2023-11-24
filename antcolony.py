# ant colony approach

import numpy as np
import random

def move_ant(ant, pheromones, matrix) :
  ant_row = ant[0]
  ant_column = ant[1]
  new_ant_row = 0
  new_ant_column = 0
  #If the ant is in the first row, it can only go right or down
  if ant_row == 0 :
    #If the pheromone is bigger for the right neigbhour, move the ant right
    if ant_column < len(matrix[0]) - 1 and pheromones[ant_row][ant_column+1] > pheromones[ant_row+1][ant_column]:
      new_ant_row = ant_row
      new_ant_column = ant_column +1
    #If the pheromone is bigger for the down neigbhour, move the ant down
    elif ant_column < len(matrix[0]) - 1 and pheromones[ant_row +1][ant_column] > pheromones[ant_row][ant_column +1]:
      new_ant_row = ant_row+1
      new_ant_column = ant_column
    else :
      random_direction = random.choice([(0,1)],[1,0])
      new_ant_row = ant_row + random_direction[0]
      new_ant_column = ant_column + random_direction[1]
    
