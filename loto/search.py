def rechercheDichotomiqueIteratif(list, n):  #itératif
    début = 0
    fin = len(list)
    trouvé = False
    while début<=fin and not trouvé :
        milieu = (début+fin)//2
        if list[milieu] == n:
            trouvé=True
        elif list[milieu]<x:
            début = milieu+1
        else:
            fin = milieu-1
    if trouvé:
        return(milieu)
    else:
        return f"{n} n'existe pas dans la list"


def rechercheDichotomiqueRecursive(list, n, gauche, droite): #récurcif
    if gauche > droite:
        return f"{n} n'existe pas dans la list"
    milieu = (gauche + droite) // 2
    if list[milieu] == n:
        return milieu
    elif list[milieu] > n:
        return rechercheDichotomiqueRecursive(list, n, gauche, milieu-1)
    else:
        return rechercheDichotomiqueRecursive(list, n, milieu+1, droite)