import numpy as np
qqch = [0,1]

def tirage(seed):
    tir = np.random.randint(low = 1, high = 45, size = 5)
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
