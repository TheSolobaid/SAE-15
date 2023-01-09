while True:
    fact = 1
    x = int(input("nombre a factorialiser: "))
    for i in range (1 , x+1):
        fact *= i
    print(f"{x}! = {fact}")