'''
def primos(numero=100):
    for y in(x for x in range(numero) if x % 2 == 1):
        print(y)
'''
'''
def primos(k):
    if k < 2:
        return False
    for x in range(2,k - 1):
        if k % x == 0:
            return False
    return True
def gerador_primo(fim=50):
    n = 2
    while n <= fim:
        if primos(n):
            yield n
        n +=1
for x in(x for x in gerador_primo()):
    print(x)
'''
def primos(fim=50):
    n = 2
    while n <= fim:
        divisor = 2
        while divisor < n:
            if n % divisor == 0:
                break
            divisor += 1
        else:
            yield n
        n += 1
for y in(x for x in primos()):
    print(y)

