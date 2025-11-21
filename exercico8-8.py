def mdc(a,b):
    print(f"Calculando mdc({a}, {b})")
    if b == 0:
        print(f"Retornando {a} porque b é 0")
        return a
    else:
        return mdc(b,a % b)
def mmc(a,b):
    return abs(a * b)/(mdc(a,b))
print(mmc(6,8))
