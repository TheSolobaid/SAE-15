import numpy as np
from numpy.random import choice
import pandas as pd
import os.path
binary = [0,1]
save = [1,2,3]
moyen = [1,2]

def tirage(j):
    tirTotal = []
    for i in range(j):
        tir = np.random.choice(np.arange(1, 46), 5, replace=False)
        tirTotal.append(tir)
    return pd.DataFrame(tirTotal, columns=['1st nbr','2nd nbr','3rd nbr','4th nbr','5th nbr'])



def testnbr(n):
    try:
        int(n)
        if int(n)>0:
            return True
        else:
            return False
    except:
        return False


def testchoice(n):
    try:
        int(n)
        if int(n) in binary:
            return True
        else:
            return False
    except:
        return False


def testseed(n):
    try:
        int(n)
        if int(n) > 0:
            return True
        else:
            return False
    except:
        return False


def testname(name , format):
    réussi = True
    if name != 'none':
        path = os.path.join(__file__.replace("test.py",""), "output")
        if int(format) == 1:
            if not name.endswith(".csv"):
                name = name+'.csv'
        if int(format) == 2:
            if not name.endswith(".json"):
                name = name+'.json'
        if int(format) == 3:
            if not name.endswith(".pkl"):
                name = name+'.pkl'
        path = os.path.join(path, name)
        if os.path.isfile(path):
            réussi = False
    else:
        réussi = False
    return réussi

def testsave(n):
    try:
        int(n)
        if int(n) in save:
            return True
        else:
            return False
    except:
        return False


def testmoyen(n):
    try:
        int(n)
        if int(n) in moyen:
            return True
        else:
            return False
    except:
        return False


def testrecherche(n):
    temp =[]
    for i in range (1, 46):
        temp.append(i)
    try:
        int(n)
        if int(n) in temp:
            return True
        else:
            return False
    except:
        return False


def testsorted(name):
    sorted = False
    if ('_sorted') in name:
        sorted = True
    return sorted
