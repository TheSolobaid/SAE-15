from test import testnbr, testchoice, tirage , testseed
import numpy as np
import pandas as pd
from tri import TriCocktail

nbr , test , seed , choice= 'a' , 'a' , 'a' , 'a'

while True:
    while not testnbr(nbr):                                                                         #test si bien nbr appartiens a N (nombre entier positif)
        nbr = input("combien de tirage voulez vous faire ?  ")
        testnbr(nbr)
        if not testnbr(nbr):
            print("ceci n'est pas une valeur acceptable (nombre positif)\n")
    while not testchoice(test):                                                                     #test si bien 0/1 et rien d'autre
        test = input("voulez vous utiliser une seed (graine aléatoir)? (oui = 1 / non = 0) ? ")
        testchoice(test)
        if not testchoice(test):
            print("ceci n'est pas une valeur acceptable (0/1)\n")
    while not testseed(seed):                                                                       #test si seed est bien entier positif
        if int(test) == 1:
            seed = input("quelle est votre seed ? ")
            if not testseed(seed):
                print("ceci n'est pas une valeur acceptable (nombre positif)\n")
        else:
            seed = np.random.randint(1000)                                                          #si pas de seed donnée en génère une et la print
            print(f"la seed utilisée est {seed} \n")
    np.random.seed(int(seed))
    print(tirage(int(nbr)))
    nbr , test , seed = 'a' , 'a' , 'a' 