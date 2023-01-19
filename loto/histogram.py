import matplotlib.pyplot as plt
import numpy as np

def histogram(df):
    fréquence = df.stack().value_counts()
    plt.bar(fréquence.index, fréquence.values)
    plt.xticks(np.arange(1,46))
    plt.xlabel('Nombre')
    plt.ylabel('fréquence')
    plt.show()
