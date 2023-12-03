import numpy as np
import random
def greedy(matrice):
    ligne = len(matrice)
    colonne = len(matrice[0])

    somme_max = matrice[0][0]
    somme_local = matrice[0][0]
    indice_coin_sup = (0, 0)
    indice_coin_inf = (0, 0)
    sous_matrice_max = [[matrice[0][0]]]

    for i in range(ligne):
        for j in range(colonne):
            if i != 0 or j != 0:
                if somme_local < 0:
                    somme_local = 0
                    indice_coin_sup = (i, j)
                somme_local = somme_local + matrice[i][j]
                if somme_local > somme_max:
                    somme_max = somme_local
                    indice_coin_inf = (i, j)
                    sous_matrice_max = [ligne[indice_coin_sup[1]:(indice_coin_inf[1] + 1)] 
                                        for ligne in matrice[indice_coin_sup[0]:(indice_coin_inf[0] + 1)]]

    return somme_max, indice_coin_sup, indice_coin_inf, sous_matrice_max


def create_random_matrix(rows, cols, min_value=0, max_value=10, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(min_value, max_value, size=(rows, cols))

def run_tests(matrix_sizes, seed):
    for size in matrix_sizes:
        rows, cols = size
        matrixx = create_random_matrix(rows, cols, seed=seed)
        somme_max, indice_coin_sup, indice_coin_inf, sous_matrice_max = greedy(matrixx)
        print(somme_max)
        for ligne in sous_matrice_max:
            print(ligne)

# This is the seed, it's fixed so it can allow us to have the same matrixes
seed_value = 42

# This is a list containing the size of each matrix that will be created
matrix_sizes_to_test = [(3, 3), (5, 5), (10, 10), (100, 100)]

run_tests(matrix_sizes_to_test, seed_value)
# c'est pour éviter de revisiter la première cellule