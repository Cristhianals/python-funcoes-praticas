# 🔤 Jogo da Forca com Palavra Aleatória

## 📋 Enunciado  
Dado o programa original:

```python
palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(50):
    print()
digitados = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "_"
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
        print("X  0  " if erros >= 1 else "X")
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
            break
```

## ➡️ Tarefa

**Alterar o programa para escolher a palavra secreta usando números aleatórios**, ou seja:

- Criar uma lista de palavras.
- Sortear uma delas com `random.randint()` ou `random.choice()`.

---

## 🧠 Objetivo do exercício

- Trabalhar com listas e seleção aleatória.
- Reforçar manipulação de strings (`lower`, `strip`).
- Praticar loops, listas e validação de tentativas repetidas.
- Entender atualização gradual da “forca”.

---


## 🚀 Código da solução  

O código completo está disponível em **[solucao.py](./solucao.py)**.

---

## 🖨 Exemplo de execução 

```text
_ _ _ _ _ _
Digite uma letra: p
p _ _ _ _ _
Digite uma letra: x
Você errou.
X==:==
X  :
X  0
X
X
===========

Digite uma letra: o
p o _ _ _ _
...

```

---

## 📚 Aprendizado

- Como sortear elementos de uma lista usando random.randint().
- Como esconder e revelar letras conforme acertos.
- Como evitar tentativas duplicadas.
- Como construir a forca passo a passo.
- Como usar listas para armazenar acertos e erros.
- Como atualizar dinamicamente a “senha” com underscores.

---

## 🔧 Extras: Melhorias possíveis

- Usar `random.choice(palavras)` (mais simples).
- Mostrar letras já tentadas.
- Criar contador de acertos/erros.
- Transformar o jogo em função reutilizável.
- Adicionar desenho da forca mais detalhado.
- Fazer versão com interface gráfica.