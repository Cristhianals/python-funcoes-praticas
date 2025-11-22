# 🔢 Função Recursiva MDC (Maior Divisor Comum)  

## 📋 Enunciado  
Escreva uma função **recursiva** que calcule o **Maior Divisor Comum (MDC)** entre dois números `a` e `b`, assumindo que `a > b`.  

A função deve seguir a regra:

\[
mdc(a, b) = 
\begin{cases} 
a & \text{se } b = 0 \\
mdc(b, a \% b) & \text{caso contrário} 
\end{cases}
\]

💡 **Exemplos esperados:**
- `mdc(12, 8)` → 4  
- `mdc(25, 5)` → 5  
- `mdc(15, 9)` → 3  

---

## 💡 Objetivo do exercício  
- Praticar **recursão** em Python.  
- Entender o algoritmo de **Euclides** para MDC.  
- Aprender a controlar chamadas recursivas e condição de parada (`base case`).  
- Retornar valores corretos através da função recursiva.

---

## 🧠 Explicação do raciocínio  
1. O algoritmo de **Euclides** diz que o MDC de dois números `a` e `b` pode ser calculado usando `mdc(b, a % b)`.  
2. A função recursiva termina quando `b == 0`, retornando `a`.  
3. A cada chamada recursiva, os valores diminuem até atingir a condição de parada.  
4. A utilização do operador `%` (`a % b`) substitui a subtração repetida e é mais eficiente.  

💡 **Dica:** imprimir cada chamada ajuda a visualizar a recursão e entender o fluxo.

---

## 🚀 Código da solução 

O código completo está disponível em **[solucao.py](./solucao.py)**  

---

## 🖨 Exemplo de execução

```text
Calculando mdc(12, 8)
Calculando mdc(8, 4)
Calculando mdc(4, 0)
Retornando 4 porque b é 0
4
Calculando mdc(25, 5)
Calculando mdc(5, 0)
Retornando 5 porque b é 0
5
Calculando mdc(15, 9)
Calculando mdc(9, 6)
Calculando mdc(6, 3)
Calculando mdc(3, 0)
Retornando 3 porque b é 0
3
```

---

## 📚 Aprendizado

- Como criar funções recursivas em Python.
- Entender o algoritmo de Euclides para cálculo do MDC.
- Importância de caso base (b == 0) para evitar recursão infinita.
- Uso do operador % para simplificar a lógica matemática.
- Visualizar o fluxo de execução recursiva com print.

