# Função Área do Triângulo 🔺

## 📝 Enunciado
Escreva uma função que receba a base e a altura de um triângulo e retorne sua área, usando a fórmula:  
**A = (base * altura) / 2**

💡 **Valores esperados**
- `area_triangulo(6, 9)` → 27  
- `area_triangulo(5, 8)` → 20  

---

## 🎯 Objetivo do exercício
- Praticar a criação de funções com múltiplos parâmetros.  
- Aplicar operadores aritméticos para calcular áreas.  
- Retornar valores numéricos a partir de funções.  

---

## 🧮 Explicação do raciocínio
A função `area_triangulo` recebe a base (`a`) e a altura (`b`) e calcula a área usando a fórmula clássica: `(a * b) / 2`.  
É uma forma direta de encapsular a fórmula matemática dentro de uma função, facilitando reutilização e leitura do código.  

---

## 🚀 Código da solução

O código completo está disponível em [solucao.py](./solucao.py)

---

## 🖨 Exemplo de execução
```text
area_triangulo(6, 9)  
16 
area_triangulo(5, 8)
81  
```

---

## 💡 **Dica:**  
Também é possível calcular a área usando funções built-in e simplificando operações:  

```python
def area_triangulo(base, altura):
    return base * altura / 2

```

---

## 📚 Aprendizado

- Como criar funções com múltiplos parâmetros em Python.
- Como aplicar fórmulas matemáticas dentro de funções.
- Como encapsular cálculos simples para reutilização.
- Interpretar e validar fórmulas matemáticas em código.

---

## ✨ Extra: Possíveis melhorias

- Validar se base e altura são números positivos.
- Criar funções semelhantes para outras figuras geométricas (quadrado, retângulo, círculo).
- Explorar fórmulas alternativas, como usando semiperímetro e teorema de Heron para triângulos gerais.