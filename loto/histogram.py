import matplotlib.pyplot as plt
l=[]
for i in range(45):
    l.append(i+1)
def histogram(dF):
    plt.hist(dF, bins=45, facecolor='g')
    plt.xticks(l)
    plt.xlabel('valleur')
    plt.ylabel("nbr de fois qu'il apparêt")
    plt.title('Histogram')
    plt.show()
