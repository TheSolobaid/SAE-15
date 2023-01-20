import matplotlib.pyplot as plt
import numpy as np

def histogramme(df):
    histo = {} 
    for col in df.columns: 
        for val in df[col]: 
            if val in histo:
                histo[val] += 1 
            else:
                histo[val] = 1 
    plt.bar(histo.keys(), histo.values()) 
    plt.xticks(np.arange(1,46))
    plt.xlabel('Nombre')
    plt.ylabel('fréquence')
    plt.show() 