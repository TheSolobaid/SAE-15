from test import testnbr, testseed, tirage
import numpy as np

nbr = 'a'
test = 'a'


while True:
    while not testnbr(nbr):
        nbr = input("combien de tirage voulez vous faire ?  ")
        testnbr(nbr)
        if not testnbr(nbr):
            print("ceci n'est pas une valeur acceptable (nombre positif)")
    while not testseed(test):
        test = input("voulez vous utiliser une seed ? (oui = 1 / non = 0) ? ")
        testseed(test)
        if not testseed(test):
            print("ceci n'est pas une valeur acceptable (0/1)")
    if int(test) == 1:
        seed = int(input("quelle est votre seed ? "))
    else:
        seed = numpy.random.randint(100)
        print(f"la seed utilisée est {seed}")
    np.random.seed(seed)
    for i in range(int(nbr)):
        print(tirage(seed))
    nbr = 'a'
    test = 'a'