def TriCocktail(list): #itératif
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


def triInsertion(list):
    swap=True
    while swap:
        swap = False
        for i in range(len(list)):
            for j in range(i , -1 , -1):                    #recule dans la liste à partire de i jusqu'au début en allant de -1 en -1
                if list[j]>list[i]:
                    list[j], list[i] = list[i], list[j]
                    swap = True
            print(list)


def triFusion(list): 
    if len(list)>1:
        m = len(list) // 2     #trouve le milieu de la liste
        l = list[:m]           #créer une liste l (gauche) avec la partie gauche
        r = list[m:]           #créer une liste r (droite) avec la partie droite
        triFusion(l)        
        triFusion(r)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):    # [...] [...]
            if l[i] < r[j]:
                list[k] = l [i]
                i += 1
            else:
                list[k] = r[j]
                j += 1
            k += 1
        while i < len(l):                   # [...] []
            list[k] = l[i]
            i += 1
            k += 1
        while j < len(r):                   # [] [...]
            list[k] = r[j]
            j += 1
            k += 1