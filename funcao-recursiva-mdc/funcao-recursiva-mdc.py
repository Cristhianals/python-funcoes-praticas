def mdc(a,b):
    print(f"Calculando mdc({a}, {b})")
    if b == 0:
        print(f"Retornando {a} porque b é 0")
        return a
    else:
        return mdc(b,a % b)
print(mdc(12, 8))  
print(mdc(25, 5))  
print(mdc(15, 9))
