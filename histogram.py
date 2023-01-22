import matplotlib.pyplot as plt
import numpy as np

def histogramme(df):
    valuelist = {} 
    for colonne in df.columns: 
        for valeur in df[colonne]: 
            if valeur in valuelist:
                valuelist[valeur] += 1 
            else:
                valuelist[valeur] = 1 
    plt.bar(valuelist.keys(), valuelist.values()) 
    plt.xticks(np.arange(1,46))
    plt.xlabel('Nombre')
    plt.ylabel('fréquence')
    plt.show() 