import numpy as np
binary = [0,1]
from numpy.random import choice
import pandas as pd
nbr = np.arange(1, 46)
import os.path

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


def testname(n):
    if os.path.isfile(n):
        return False
