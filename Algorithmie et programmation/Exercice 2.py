def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)

while True:
    n = int(input("nombre a factorialiser: "))
    print(factoriel(n))