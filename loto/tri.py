
def triFusion(l): 
    if len(l)>1:
        m = len(l) // 2     #trouve le millieu de la liste
        g = l[:m]           #créer une liste g (gauche) avec la partie gauche
        d = l[m:]           #créer une liste d (droite) avec la partie droite
        triFusion(d)        
        triFusion(g)
        i, j, k = 0, 0, 0
        while i < len(g) and j < len(d):    # [...] [...]
            if g[i] < d[j]:
                l[k] = g [i]
                i += 1
            else:
                l[k] = d[j]
                j += 1
            k += 1
        while i < len(g):                   # [...] []
            l[k] = g[i]
            i += 1
            k += 1
        while j < len(d):                   # [] [...]
            l[k] = d[j]
            j += 1
            k += 1


def TriCocktail(list): ##itératif
    debut = 0
    fin = len(list)
    test = 1
    while test == 1:
        test = 0
        for i in range(debut, fin - 1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list [i+1]
                list[i+1] = temp
                test = 1
        fin -= 1
        for i in range(fin - 2, debut -1, -1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list [i+1]
                list[i+1] = temp
                test = 1
        debut += 1