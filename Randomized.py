import numpy as np
import random


def somme_max_segment_matrice_aleatoire(alea, matrice):
    lignes = len(matrice)
    colonnes = len(matrice[0])
    somme_max = float('-inf')
    coins_max = None
    
    for nbr_alea in range(alea):
        debut_ligne = random.randint(0, lignes - 1)
        fin_ligne = random.randint(debut_ligne, lignes - 1)
        debut_colonne = random.randint(0, colonnes - 1)
        fin_colonne = random.randint(debut_colonne, colonnes - 1)
        
        somme_local = 0
        for i in range(debut_ligne, fin_ligne + 1):
            somme_ligne = sum(matrice[i][debut_colonne:fin_colonne + 1])
            somme_local = somme_local +  somme_ligne
        
        if somme_local > somme_max:
            somme_max = somme_local
            coins_max = ((debut_ligne, debut_colonne), (fin_ligne, fin_colonne))
    
    return somme_max, coins_max




        


def create_random_matrix(rows, cols, value_interval=(-3, 10), seed=None):
    if seed is not None:
        np.random.seed(seed)
    min_value, max_value = value_interval
    return np.random.randint(min_value, max_value, size=(rows, cols))

def run_tests(matrix_sizes, value_intervals, seed):
    for size in matrix_sizes:
      for value_interval in value_intervals :
        rows, cols = size
        matrixx = create_random_matrix(rows, cols, value_interval, seed=seed)
        print("--- matrice test ---\n",matrixx)
        resultat, indices = somme_max_segment_matrice_aleatoire(100000, matrixx)
        coin_sup, coin_inf = indices

      
        print("> somme maximal", resultat)
        print("> indice du coin supérieur de la sous-matrice ", coin_sup, " du coin inférieur ", coin_inf)

        print("--- Sous-matrice maximal ---")
        for i in range(coin_sup[0], coin_inf[0] + 1):
            for j in range(coin_sup[1], coin_inf[1] + 1):
                print(matrixx[i][j], end=" ")
            print()


# Fixed Seed value to have the same test matrices
seed_value = 42

# Adding the size of our matrices
matrix_sizes_to_test = [(3, 3), (15, 30),(100, 100)]
# Adding value intervals for each matrix
matrix_value_intervals = [(-50, -1),(-25,25),(10,100)]

# Execute the tests with the same random seed
run_tests(matrix_sizes_to_test, matrix_value_intervals, seed_value)
