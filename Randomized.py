import numpy as np
import random

def somme_max_segment_matrice_aleatoire(alea,matrice):
    ligne = len(matrice)
    colonne = len(matrice[0])
    somme_max = float('-inf')
    coins = None
    
    for nbr_alea in range(alea): 
        debut_ligne = random.randint(0, ligne - 1)
        fin_ligne = random.randint(debut_ligne, ligne - 1)
        debut_colonne = random.randint(0, colonne - 1)
        fin_colonne = random.randint(debut_colonne, colonne - 1)
        
        somme_courante = 0
        for i in range(debut_ligne, fin_ligne + 1):
            for j in range(debut_colonne, fin_colonne + 1):
                somme_courante = somme_courante + matrice[i][j]
                if somme_courante > somme_max:
                    somme_max = somme_courante
                    coins = ((debut_ligne, debut_colonne), (fin_ligne, fin_colonne))
                if somme_courante < 0:
                    somme_courante = 0
    
    return somme_max, coins

def create_random_matrix(rows, cols, min_value=0, max_value=10, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(min_value, max_value, size=(rows, cols))

def run_tests(matrix_sizes, seed):
    for size in matrix_sizes:
        rows, cols = size
        matrixx = create_random_matrix(rows, cols, seed=seed)
        resultat, indices = somme_max_segment_matrice_aleatoire(100000,matrixx)
        coin_sup, coin_inf = indices

        print("La somme maximale du segment dans la matrice est :", resultat)
        print("Indices du coin supérieur de la sous-matrice :", coin_sup)
        print("Indices du coin inférieur de la sous-matrice :", coin_inf)

        print("Sous-matrice correspondante :")
        for i in range(coin_sup[0], coin_inf[0] + 1):
            for j in range(coin_sup[1], coin_inf[1] + 1):
                print(matrixx[i][j], end=" ")
            print()

# This is the seed, it's fixed so it can allow us to have the same matrixes
seed_value = 42

# This is a list containing the size of each matrix that will be created
matrix_sizes_to_test = [(3, 3), (5, 5), (10, 10), (100, 100)]

run_tests(matrix_sizes_to_test, seed_value)