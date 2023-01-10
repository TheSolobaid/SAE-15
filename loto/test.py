import numpy as np
qqch = [0,1]
from numpy.random import choice
nbr = np.arange(1, 46)


def tirage():
    tir = choice(nbr, size=5, replace=False)
    return tir


def testnbr(n):
    try:
        int(n)
        if int(n)>0:
            return True
        else:
            return False
    except:
        return False


def testseed(n):
    try:
        int(n)
        if int(n) in qqch:
            return True
        else:
            return False
    except:
        return False


def testnbseed(n):
    try:
        int(n)
        if int(n) > 0:
            return True
        else:
            return False
    except:
        return False