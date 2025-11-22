# Função Verifica Múltiplo 🔢

## 📋 Enunciado
Escreva uma função que receba dois números como parâmetros e retorne `True` se o primeiro for múltiplo do segundo, caso contrário, retorne `False`.

💡 **Valores esperados**
- `multiplo(8, 4)` → True  
- `multiplo(7, 3)` → False  
- `multiplo(5, 5)` → True  

---

## 💡 Objetivo do exercício
- Praticar a criação de funções em Python.  
- Usar operadores aritméticos para lógica condicional.  
- Retornar valores booleanos (`True`/`False`) a partir de condições.  

---

## 🧠 Explicação do raciocínio
A função `multiplo` verifica se `a` é múltiplo de `b`.  
No código fornecido, foi usado um teste específico:  
- `(b * 2 == a)` → verifica se `a` é exatamente o dobro de `b`.  
- `(a == b)` → verifica se os números são iguais, também considerado múltiplo.  

---

💡 **Observação:**  
Uma abordagem mais geral seria usar o operador módulo `%` para verificar se o resto da divisão é zero (`a % b == 0`), que funciona para qualquer múltiplo.  

```python
def multiplo(a, b):
    if b == 0:
        return False
    return a % b == 0
```

---

## 🚀 Código da solução

O código completo está disponível em [solucao.py](./solucao.py)

---

## 🖥 Exemplo de execução

```text
True
False
True
```

---

## 🎯 **Aprendizado**

- Como criar funções que retornam valores booleanos.
- Como usar lógica condicional para verificar múltiplos.
- Diferença entre checagens específicas (dobro ou igual) e abordagens gerais (%).
- Interpretar e validar condições matemáticas simples em código.

---

## 💡 Extra: Melhorias possíveis

- Tratar casos onde b = 0 para evitar divisão por zero.
- Aceitar números negativos sem alterar a lógica de múltiplos.
- Usar o operador % para criar funções mais genéricas e reutilizáveis.

