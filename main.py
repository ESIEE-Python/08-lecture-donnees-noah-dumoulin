#### Imports et définition des variables globales
#import random
'''lecture de données noah dumoulin'''
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        l=[list(map(int, line.strip().split(';')))for line in file.readlines()]
    return l

def get_list_k(data, k):
    "retoune la liste de toutes les datas"
    if 0<=k<len(data):
        l=data[k]
    else:
        l=None
    return l

def get_first(l):
    '''donne le premier élement de l'''
    return l[0] if l else None

def get_last(l):
    '''donne le dernier élement de l'''
    return l[-1] if l else None

def get_max(l):
    '''donne l'élement le plus grand de l'''
    return max(l) if l else None

def get_min(l):
    '''retourne le plus petit élement'''
    return min(l) if l else None

def get_sum(l):
    '''renvoie la somme des élement'''
    return sum(l) if l else None


#### Fonction principale


def main():
    '''main'''
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
