# Função Área do Quadrado ⬛

## 📋 Enunciado

Escreva uma função que receba o lado de um quadrado e retorne sua área, usando a fórmula:  
**A = lado²**

💡 **Valores esperados**
- `area_quadrado(4)` → 16  
- `area_quadrado(9)` → 81  

---

## 💡 Objetivo do exercício

- Praticar a criação de funções em Python.  
- Aplicar operadores aritméticos (`**`) para calcular potências.  
- Retornar valores numéricos a partir de funções.  

---

## 🧠 Explicação do raciocínio

A função `area_quadrado` recebe o comprimento do lado do quadrado e retorna o quadrado desse valor (`lado ** 2`).  
É uma maneira direta de calcular a área usando operadores matemáticos do Python, sem necessidade de loops ou condicionais.

---

## 🚀 Código da solução

O código completo está disponível em **[função-área-quadrado.py](./função-área-quadrado.py)**

---

## 🖥 Exemplo de execução

```text
area_quadrado(4)  
16 
area_quadrado(9)
81  
```
---

💡 **Curiosidade:**  
Outra forma de calcular a área de um quadrado seria usando a função `pow()` do Python:  

```python
def area_quadrado(lado):
    return pow(lado, 2)
```

---

## 🎯 **Aprendizado**

- Como criar funções simples que retornam valores numéricos.
- Como usar operadores matemáticos (**) em Python.
- Como funções podem encapsular fórmulas matemáticas para reutilização.
- Entender que Python oferece funções built-in, como pow(), que podem substituir operadores.

