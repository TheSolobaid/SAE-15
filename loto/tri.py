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
                ##print(list)
        fin -= 1
        for i in range(fin - 2, debut -1, -1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list [i+1]
                list[i+1] = temp
                test = 1
                ##print(list)
        debut += 1