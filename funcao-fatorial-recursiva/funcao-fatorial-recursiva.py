def fatorial(n):
    print(f"calculando o fatorial de {n}")
    if n == 0 or n == 1:
        print(f"fatorial de {n} = 1")
        return 1
    else:
        fat = n * fatorial(n-1)
        print(f"fatorial de {n} = {fat}")
        return fat
print(fatorial(4))
'''
Vamos analisar fatorial(4) passo a passo
Chamamos fatorial(4), aí ele faz o seguinte:

Passo 1: fatorial(4)
return 4 * fatorial(3)

Passo 2: fatorial(3)
return 3 * fatorial(2)

Passo 3: fatorial(2)
return 2 * fatorial(1)

Passo 4: fatorial(1)
Aqui é o caso base, então retorna 1 diretamente:
return 1

Agora voltamos com os valores (como uma pilha):
fatorial(1) → retorna 1

fatorial(2) → vira 2 * 1 → 2

fatorial(3) → vira 3 * 2 → 6

fatorial(4) → vira 4 * 6 → 24

Resposta final:
print(fatorial(4))  Resultado: 24
Dica para pensar em recursão:
Pense assim:
"Essa função vai confiar que a função 'menor' já sabe fazer seu trabalho,
e vou só multiplicar o meu número por ela."
'''
