from test import testnbr, testseed, tirage , testnbseed
import numpy as np
from tri import TriCocktail

nbr = 'a'
test = 'a'
seed = 'a'
choice = 'a'
while True:
    while not testnbr(nbr):
        nbr = input("combien de tirage voulez vous faire ?  ")
        testnbr(nbr)
        if not testnbr(nbr):
            print("ceci n'est pas une valeur acceptable (nombre positif)\n")
    while not testseed(test):
        test = input("voulez vous utiliser une seed (graine aléatoir)? (oui = 1 / non = 0) ? ")
        testseed(test)
        if not testseed(test):
            print("ceci n'est pas une valeur acceptable (0/1)\n")
    while not testnbseed(seed):
        if int(test) == 1:
            seed = input("quelle est votre seed ? ")
            if not testnbseed(seed):
                print("ceci n'est pas une valeur acceptable (nombre positif)\n")
        else:
            seed = np.random.randint(1000)
            print(f"la seed utilisée est {seed} \n")
    np.random.seed(int(seed))
    for i in range(int(nbr)):
        print(tirage())
    nbr = 'a'
    test = 'a'
    seed = 'a'
    while not testseed(choice):
        choice = input("voulez-vous trier ? (oui = 1 / non = 0) ? ")
        testseed(choice)
        if not testseed(choice):
            print("ceci n'est pas une valeur acceptable (0/1)\n")
   # if choice==1:
