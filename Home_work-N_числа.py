import random
print('How the number?')
n = random.randint(1, 100)
print(n)
a = 0
g = None
while g != n:
    g = int(input('Enter a number:', ))
    a += 1
    if g < n:
        print('+')
    elif g > n:
        print('-')
    print(f"Вгадав:{a}")
