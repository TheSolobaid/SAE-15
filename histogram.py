import matplotlib.pyplot as plt
import numpy as np

def histogramme(df):
    histo = {} 
    for colonne in df.columns: 
        for valeur in df[colonne]: 
            if valeur in histo:
                histo[valeur] += 1 
            else:
                histo[valeur] = 1 
    plt.bar(histo.keys(), histo.values()) 
    plt.xticks(np.arange(1,46))
    plt.xlabel('Nombre')
    plt.ylabel('fréquence')
    plt.show() 