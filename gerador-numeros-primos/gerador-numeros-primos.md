# 🔢 Gerador de Números Primos com `yield`

## 📋 Enunciado  
Escreva um **gerador** capaz de produzir a série dos **números primos**.  
O gerador deve receber um valor limite (opcional) e produzir, um por vez, todos os primos até esse limite.

---

## 💡 Objetivo do exercício  
- Entender como criar funções geradoras com `yield`.  
- Identificar números primos sem usar recursão.  
- Criar loops aninhados para varrer divisores.  
- Practicar a técnica do `for/else`.  
- Entender o papel de geradores para economizar memória.  

---

## 🧠 Explicação do raciocínio  
Para gerar números primos:

1. **Percorremos todos os números começando em 2**, até o valor final.  
2. Para cada número `n`, testamos se ele possui algum divisor além de 1 e dele mesmo.  
3. Esse teste é feito com um loop de `divisor = 2` até `divisor < n`.  
4. Se encontrarmos um divisor → **não é primo** → interrompe com `break`.  
5. Se **não houver `break`**, o bloco `else` do `while` é executado:  
   → significa que o número é primo, então usamos **`yield n`**.  
6. A função retorna um número por vez, economizando memória e permitindo processamento sob demanda.

---

## 🚀 Código da solução

O código completo está disponível em **[solucao.py](./solucao.py)**.

---

## 🖨 Exemplo de execução

```python
for y in(x for x in primos()):
    print(y)
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47

```

---

## 🎯 Aprendizado

- Como funciona um gerador `(yield)` em Python.
- Diferença entre retornar valores e produzi-los sob demanda.
- Uso do `while` com `for/else` para testar primalidade.
- Como funciona a lógica de detecção de divisor.
- Importância do `break` para interromper a verificação.
- Como um gerador permite iterar listas infinitamente grandes sem gastar memória.

