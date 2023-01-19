import numpy as np
import pandas as pd
from test import testnbr, testchoice, tirage , testseed, testsave, testname, testmoyen, testrecherche, testsorted
from search import rechercheDichotomiqueIteratif, rechercheDichotomiqueRecursive
from tri import TriCocktail , triFusion , triInsertion
from exportSAVE import exportCSV, exportJSON, exportPICKLE
from importSAVE import importCSV, importJSON, importPICKLE
from histogram import histogram


while True:
    nbr,test,seed,save,choice,format,sorting,way,recher,moyen,recherche,name,charge='a','a','a','a','a','a','a','a','a','a','a','none','a'          #déclaration de valeur fausse pour pouvoir rentrer dans les boucles de test
    iteration = 0
    chargedata = False
    sorted = False


            #chargement de donnée
    while not testchoice(charge):
        charge = input("voulez vous charger des données déjà générées? (1 = oui / 0 = non)? ")
        if not testchoice(charge):
            print("ceci n'est pas une valeur acceptable (0/1)\n")
    if int(charge) == 1:                                                                                     
        chargedata = False
        while not testsave(format):
            format = input("quel est le format d'enregistrement de vos données? (.csv = 1 / .json = 2 / .pkl = 3)? ")
            if not testsave(format):
                print("ceci n'est pas une valeur acceptable (1/2/3)\n")
        if int(format) == 1:    
            name = input('nom de la sauvegarde: ')
            tir = importCSV(name)
            chargedata = True
        if int(format) == 2:    
            name = input('nom de la sauvegarde: ')
            tir = importJSON(name)
            chargedata = True
        if int(format) == 3:   
            name = input('nom de la sauvegarde: ')
            tir = importPICKLE(name)
            chargedata = True
        format = 'a'
        if testsorted(name):
            sorted = True
        print(tir)


    if not chargedata:
            #génération de donnée si besoin
        while not testnbr(nbr):                                                                         #test si bien nbr appartiens a N (nombre entier positif)
            nbr = input("\n--------------------------------------\n\ncombien de tirage voulez vous faire ?  ")
            if not testnbr(nbr):
                print("ceci n'est pas une valeur acceptable (nombre positif)\n")
        while not testchoice(test):                                                                     #test si bien 0/1 et rien d'autre
            test = input("voulez vous utiliser une seed (graine aléatoir)? (oui = 1 / non = 0) ? ")
            if not testchoice(test):
                print("ceci n'est pas une valeur acceptable (0/1)\n")
        while not testseed(seed):                                                                       #test si seed est bien entier positif
            if int(test) == 1:
                seed = input("quelle est votre seed ? ")
                if not testseed(seed):
                    print("ceci n'est pas une valeur acceptable (nombre positif)\n")
            else:
                seed = np.random.randint(1000)                                                          #si pas de seed donnée en génère une et la print
                print(f"\n--------------------------------------\n\nla seed utilisée est {seed} \n")
        np.random.seed(int(seed))
        tir=tirage(int(nbr))
        print(tir)


        #test sorting data
    if not sorted:
        while not testchoice(sorting):
            sorting = input("\n--------------------------------------\n\nvoulez vous trier vos données? (oui = 1 / non = 0)? ")
            if not testchoice(sorting):
                print("ceci n'est pas une valeur acceptable (0/1)\n")
        if int(sorting) == 1:
            while not testsave(way):
                way = input("de quelle manière? (1 = tri Cocktail / 2 = tri Fusion / 3 = tri insertion)? ")
                testsave(way)
                if not testsave(way):
                    print("ceci n'est pas une valeur acceptable (1/2/3)\n")
            if int(way) == 1:                                                                                                                        #tri cocktail
                tritotal = []
                for i in range(len(tir)):
                    templist=tir.iloc[i].values.tolist()
                    templist = TriCocktail(templist)
                    tir.iloc[i]=templist
                tir =  pd.DataFrame(tritotal, columns=['1st nbr','2nd nbr','3rd nbr','4th nbr','5th nbr'])
                sorted = True
            if int(way) == 2:                                                                                                                        #tri fusion
                tritotal = []
                for i in range(len(tir)):
                    templist=tir.iloc[i].values.tolist()
                    templist = triFusion(templist)
                    tir.iloc[i]=templist
                tir =  pd.DataFrame(tritotal, columns=['1st nbr','2nd nbr','3rd nbr','4th nbr','5th nbr'])
                sorted = True
            if int(way) == 3:                                                                                                                        #tri insertion
                tritotal = []
                for i in range(len(tir)):
                    templist=tir.iloc[i].values.tolist()
                    templist = triInsertion(templist)
                    tir.iloc[i]=templist
                tir =  pd.DataFrame(tritotal, columns=['1st nbr','2nd nbr','3rd nbr','4th nbr','5th nbr'])
                sorted = True
            print(tir)


        #sauvegarde de donnée
    while not testchoice(save):
        save = input("\n--------------------------------------\n\nvoulez vous sauvegarder votre fichier ? (oui = 1 / non = 0)? ")               #choix de sauvegarde ou non
        if not testchoice(save):
            print("ceci n'est pas une valeur acceptable (0/1)\n")
    if int(save) == 1:
        while not testsave(format):
            format = input("sous quel format? (.csv = 1 / .json = 2 / .pkl = 3)? ")      
            if not testsave(format):
                print("ceci n'est pas une valeur acceptable (1/2/3)\n")
        if int(format) == 1:    
            while not testname(name, format):
                name = input('nom de la sauvegarde: ')
                if not testname(name, format):
                    print(f"{name} est déjà le nom d'une sauvegarde, veuillez changer de nom \n")
            exportCSV(tir, name, sorted)
        if int(format) == 2:    
            while not testname(name,format):
                name = input('nom de la sauvegarde: ')
                if not testname(name,format):
                    print(f"{name} est déjà le nom d'une sauvegarde, veuillez changer de nom \n")
            exportJSON(tir, name,sorted)
        if int(format) == 3:    
            while not testname(name,format):
                name = input('nom de la sauvegarde: ')
                if not testname(name,format):
                    print(f"{name} est déjà le nom d'une sauvegarde, veuillez changer de nom \n")
            exportPICKLE(tir, name,sorted)


        #choix pour histogramme
    while not testchoice(choice):
            choice = int(input("\n--------------------------------------\n\nvoulez vous tracer un histogram? (oui = 1 / non = 0)? "))
            if not testchoice(choice):
                print("ceci n'est pas une valeur acceptable (0/1)\n")
    if choice == 1 :
        histogram(tir)

    
        #choix recherche
    while not testchoice(recher):
            recher = input("\n--------------------------------------\n\nvoulez vous rechercher un nombre précis? (oui = 1 / non = 0)? ")
            if not testchoice(recher):
                print("ceci n'est pas une valeur acceptable (0/1)\n")
    if sorted:
        if recher == 1 :
            while not testrecherche(recherche):
                recherche = input("quelle est la valeure a rechercher? (entre 1 et 45)? ")
                if not testrecherche(recherche):
                    print("ceci n'est pas une valeur acceptable (nombre entre 1 et 45)\n")
            while not testmoyen(moyen):
                moyen = input("par quelle methode ? (1 = itérative / 2 = recurcive)? ")
                if not testmoyen(moyen):
                    print("ceci n'est pas une valeur acceptable (1/2)\n")
            if int(moyen) == 1:
                for i in range(len(tir)):
                    templist=tir.iloc[i].values.tolist()
                    if rechercheDichotomiqueIteratif(templist, recherche):
                        print(f"le nombre {recherche} est dans le {i+1}e tirage à la {rechercheDichotomiqueIteratif(templist, recherche)+1}e place\n")
                        iteration +=1 
                if iteration == 0:
                    print(f"{recherche} n'est pas présent dans la liste")
                else:
                    print(f"{recherche} est {iteration} fois dans le(s) {len(tir)} tirage(s)")
            if int(moyen) == 2:
                for i in range(len(tir)):
                    templist=tir.iloc[i].values.tolist()
                    index = rechercheDichotomiqueRecursive(templist, recherche)
                    if index is not False:
                        iteration += 1
                        print(f"le nombre {recherche} est dans le {i+1}e tirage à la {index+1}e place\n")
                if iteration == 0:
                    print(f"{recherche} n'est pas présent dans la liste")
                print(f"{recherche} est {iteration} fois dans le(s) {len(tir)} tirage(s)")
    else:
        print("la recherche ne peut pas être effectuée car la liste n'est pas triée! ")
