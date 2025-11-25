# 🔢 Gerador da Sequência de Fibonacci

## 📋 Enunciado  

Escreva um **gerador** capaz de produzir a série de **Fibonacci**.  
A função deve gerar os números da sequência **sob demanda**, usando `yield`.

---

## 💡 Objetivo do exercício  

- Criar funções geradoras (`yield`) em Python.  
- Produzir elementos de uma sequência **sob demanda**, sem armazenar toda a lista.  
- Manipular variáveis temporárias para calcular o próximo número da sequência.  
- Praticar atribuição múltipla (`p, s = s, s + p`).  

---

## 🧠 Explicação do raciocínio  

1. Começamos com os dois primeiros elementos da sequência:  
   - `p = 0` (anterior)  
   - `s = 1` (atual)  
2. Em cada iteração do loop:  
   - Retornamos `s` com `yield`.  
   - Calculamos o próximo número: `p, s = s, s + p`.  
3. O loop continua enquanto `s` for menor que um limite definido (no exemplo, 10).  
4. O gerador produz **um número por vez**, permitindo economizar memória e iterar eficientemente.  

---

## 🚀 Código da solução

O código completo está disponível em **[gerador-fibonacci.py](./gerador-fibonacci.py)**.

---

## 🖨 Exemplo de execução

```python
for y in (x for x in gerador_fibonacci()):
    print(y)
1
1
2
3
5
8

```

---

## 🎯 Aprendizado

- Como criar geradores com `yield` em Python.
- Como gerar sequências infinitas ou limitadas sob demanda.
- Como usar atribuição múltipla para atualizar variáveis.
- Entender a lógica da sequência de Fibonacci.
- Economia de memória em relação a criar listas completas.