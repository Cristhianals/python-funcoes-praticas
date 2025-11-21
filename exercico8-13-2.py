import random
for x in range(3):
    n = random.randint(1,10)
    x = int(input("escolha um numero entre 1 e 10:"))
    if x == n:
        print("vc acertou")
        break
    else:
        print("vc errou.")
