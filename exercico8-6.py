def soma(l):
    total = 0
    x = 0
    for e in l:
        if x == 5:
            break
        total += e
        x += 1
    return total
l = [1,7,2,9,15]
def somaa(l):
    total = 0
    for i in range(5):
        total += l[i]
    return total
def soma(l):
    total = 0
    for i in range(min(5, len(l))):  # garante que não vai dar erro se a lista tiver < 5 elementos
        total += l[i]
    return total
print(soma(l))
print(somaa(l))
