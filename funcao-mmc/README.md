# 🟢 Função MMC (Menor Múltiplo Comum)  

## 📋 Enunciado  

Usando a função `mdc(a, b)` definida no exercício anterior, defina uma função que calcule o **Menor Múltiplo Comum (MMC)** entre dois números `a` e `b`.  

A fórmula do MMC é:  

\[
mmc(a, b) = \frac{|a \cdot b|}{mdc(a, b)}
\]

💡 **Dica em Python:** `|a * b|` pode ser escrito como `abs(a * b)`.

💡 **Exemplo esperado:**  

- `mmc(6, 8)` → 24  

---

## 💡 Objetivo do exercício  

- Praticar a **reutilização de funções** em Python.  
- Aplicar **matemática discreta** (MMC) em programação.  
- Consolidar o conceito de MDC e MMC.  
- Entender o uso de **funções auxiliares** para simplificar cálculos complexos.

---

## 🧠 Explicação do raciocínio  

1. O MMC de dois números `a` e `b` pode ser calculado a partir do produto absoluto dividido pelo MDC.  
2. Primeiro, calculamos o MDC usando a função recursiva `mdc(a, b)` do exercício anterior.  
3. Em seguida, usamos `abs(a * b) / mdc(a, b)` para obter o MMC.  
4. O uso de `abs` garante que o resultado seja sempre positivo, mesmo se algum número for negativo.

---

## 🚀 Código da solução 

O código completo está disponível em **[funcao-mmc.py](./funcao-mmc.py)**  

---

## 🖨 Exemplo de execução

```text
Calculando mdc(6, 8)
Calculando mdc(8, 6)
Calculando mdc(6, 2)
Calculando mdc(2, 0)
Retornando 2 porque b é 0
24.0
```

---

## 📚 Aprendizado

- Como reutilizar funções em Python.
- Relação entre MDC e MMC: MMC = |a * b| / MDC(a, b).
- Uso do operador abs() para lidar com valores negativos.
- Entender como funções auxiliares tornam o código modular e mais legível.
- Consolidação de conceitos de recursão e aritmética de inteiros.