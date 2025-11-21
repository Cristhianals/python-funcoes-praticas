import random
'''
random.sample(palavras, 1)
"".join(random.sample(...))
random.sample(palavras, 1)[0]	
random.choice(palavras
'''
palavras = ["abracadabra","banana","escada","salsicha","abacate","limao","ferrugem","sal","chiclete"]
random.shuffle(palavras)
n = random.randint(0, len(palavras)-1)
palavra = palavras[n]
for x in range(40):
    print()
digitados = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "-"
    print(senha)
    if senha == palavra:
        print("voce acertou!")
        break
    tentativa = input("\ndigite uma letra:").lower().strip()
    if tentativa in digitados:
        print("voce ja tententou essa letra!")
        continue
    else:
        digitados += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("voce errou!")
        print("X==:==\nX  :  ")
        print("X  0  "if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  |  "
        elif erros == 3:
            linha2 = " \\|  "
        elif erros >= 4:
            linha2 = " \\|/ "
        print(f"X{linha2}")
        linha3 = ""
        if erros == 5:
            linha3 = " /   "
        elif erros >= 6:
            linha3 += " / \\ "
        print(f"X{linha3}")
        print("X\n===========")
        if erros == 6:
            print("enforcado")
            print("a palavra era \n{:0}".format(palavra))
            break
