import random
Ln=[]
for i in range(10):
    Ln.append(random.randint(0,20))
print(Ln)
for i in range(len(Ln)):
    for j in range(len(Ln)):
        if Ln[i] < Ln[j]:
            temp2 = Ln[j]
            Ln[j] = Ln[i]
            Ln[i] = temp2
    print(Ln)