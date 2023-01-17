def rechercheDichotomiqueIteratif(list, n):  #itératif
    début = 0
    fin = len(list)
    trouvé = False
    while début<=fin and not trouvé :
        milieu = (début+fin)//2
        if list[milieu] == int(n):
            trouvé=True
        elif list[milieu]<int(n):
            début = milieu+1
        else:
            fin = milieu-1
    if trouvé:
        return milieu
    else:
        return False


"""def rechercheDichotomiqueRecursive(list, n, gauche, droite): #récurcif
    if gauche > droite:
        return False
    milieu = (gauche + droite) // 2
    if list[milieu] == int(n):
        return milieu
    elif list[milieu] > int(n):
        return rechercheDichotomiqueRecursive(list, n, gauche, milieu)
    else:
        return rechercheDichotomiqueRecursive(list, n, milieu, droite)
"""
def rechercheDichotomiqueRecursive( list, n, gauche = 0, droite = -1 ):
    if gauche == droite: 
        return False
    else:
        if droite == -1 : 
            droite = len(list)-1
        m = (gauche+droite)//2
        if list[m] == int(n) :
            return m
        elif list[m] > int(n) :
            return rechercheDichotomiqueRecursive(list, n, gauche, m-1)
        else :
            return rechercheDichotomiqueRecursive(list, n, m+1, droite)