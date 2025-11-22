# 🔢 Função Fibonacci Sem Recursão  

## 📋 Enunciado  

Escreva uma função que calcule o *n*-ésimo termo da sequência de Fibonacci **sem utilizar recursão**.

A sequência começa assim:  
`0, 1, 1, 2, 3, 5, 8, 13, ...`

Onde cada termo é a soma dos dois anteriores.

Exemplo esperado:  
- `fibonacci(10)` → 55  

---

## 🎯 Objetivo do exercício  

- Aprender a calcular Fibonacci sem recursão.  
- Entender como o algoritmo pode ser implementado de forma iterativa.  
- Introduzir o conceito de **programação dinâmica** e otimização com uso mínimo de memória.  
- Perceber diferenças entre versões “ingênuas”, versões eficientes e diferentes formas de armazenar resultados.

---

## 🧠 Explicação do raciocínio  

Uma função Fibonacci sem recursão evita o problema da repetição de cálculos que ocorre na recursão tradicional.

O método iterativo funciona assim:

1. Começamos com os dois primeiros valores:  
   - `f0 = 0`  
   - `f1 = 1`  
2. Atualizamos os valores repetidamente até chegar ao termo desejado:  
   - `próximo = f0 + f1`  
   - `f0 = f1`  
   - `f1 = próximo`  
3. Quando o loop termina, `f1` contém o resultado.

Esse processo imita o Fibonacci clássico, porém sem recursão — mais rápido e mais eficiente.

---

## 🚀 Código da solução  

O código completo está disponível em **[solucao.py](./solucao.py)**.

---

## 🖨 Exemplo de execução

```python
print(fibonacci(10))  
55
```

---

## 📚 Aprendizado

- Como calcular Fibonacci de forma iterativa e eficiente.
- Como substituir recursão por um loop quando possível.
- Como usar duas variáveis que avançam juntas (“janelinha deslizante”) para economizar memória.
- Como comparar diferentes implementações e reconhecer a mais eficiente.
- Como raciocinar sobre atualizações sequenciais de valores.