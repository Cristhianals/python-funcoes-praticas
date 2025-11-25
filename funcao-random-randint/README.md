# 🎯 Jogo de Adivinhação com 3 Tentativas

## 📋 Enunciado  

Altere o programa abaixo:

```python
import random
for x in range(10):
    print(random.randint(1,100))
n = random.randint(1,10)
x = int(input("escolha um numero entre 1 e 10:"))
if x == n:
    print("vc acertou")
else:
    print("vc errou.")
```
De forma que:

- O usuário tenha três chances para acertar o número escolhido pelo computador.
- O programa deve terminar imediatamente se o usuário acertar.
- Caso erre nas três tentativas, o programa termina com erro.

---

## 🎯 Objetivo do exercício

- Praticar loops com número fixo de repetições.
- Reforçar o uso de break para encerrar loops antecipadamente.
- Trabalhar com geração de números aleatórios (random.randint).
- Utilizar input() para interações com o usuário.
- Criar lógica de tentativa e erro controlada.

---

## 🧠 Explicação do raciocínio

O programa precisa dar ao usuário 3 tentativas e parar quando ele acertar.
Para isso:

1. Utiliza-se um `for` com `range(3)` para garantir 3 tentativas.
2. A cada tentativa, o programa gera um novo número aleatório entre 1 e 10.
3. O usuário digita um valor pelo `input()`.
4. Se o valor for igual ao número gerado, o programa exibe “você acertou” e sai do loop com `break`.
5. Caso contrário, informa que errou e continua até completar as 3 tentativas.

Esse padrão é muito comum em jogos simples, autenticações e loops com condições de saída.

---

## 🚀 Código da solução 

O código completo está disponível em **[funcao-random-randint.py](./funcao-random-randint.py)**  

---
## 🖨 Exemplo de execução

```text
Escolha um número entre 1 e 10: 4
Você errou.
Escolha um número entre 1 e 10: 8
Você errou.
Escolha um número entre 1 e 10: 3
Você acertou!

Ou, se errar todas:

Escolha um número entre 1 e 10: 1
Você errou.
Escolha um número entre 1 e 10: 2
Você errou.
Escolha um número entre 1 e 10: 5
Você errou.

```

---

## 📚 Aprendizado

- Como usar range(3) para limitar tentativas.
- Como usar break para encerrar o loop antes do fim.
- Leitura de dados com input() e conversão para int.
- Como gerar valores aleatórios com random.randint().
- Estruturas de controle simples: repetição + decisão.