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


def rechercheDichotomiqueRecursive(liste, n, gauche = 0, droite = -2):
    if droite == -2:
            droite = len(liste) - 1
    if gauche > droite:
        return False
    else:
        milieu = (gauche + droite) // 2
        if liste[milieu] == int(n):
            return milieu
        elif liste[milieu] > int(n):
            return rechercheDichotomiqueRecursive(liste, n, gauche, milieu - 1)
        else:
            return rechercheDichotomiqueRecursive(liste, n, milieu + 1, droite)
