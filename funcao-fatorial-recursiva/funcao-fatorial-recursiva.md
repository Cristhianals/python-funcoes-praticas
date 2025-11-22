# 🧮 Função Recursiva de Fatorial  

## 📋 Enunciado  
Rastreie o programa abaixo e compare o seu resultado com o apresentado, observando as chamadas recursivas e como o valor final é construído:

```python
def fatorial(n):
    print(f"calculando o fatorial de {n}")
    if n == 0 or n == 1:
        print(f"fatorial de {n} = 1")
        return 1
    else:
        fat = n * fatorial(n-1)
        print(f"fatorial de {n} = {fat}")
        return fat

print(fatorial(4))
```

---

## 💡 Objetivo do exercício
- Entender como funciona a **recursão** passo a passo.  
- Analisar o fluxo de execução seguindo a ordem das chamadas.  
- Compreender o conceito de **caso base** e **caso recursivo**.  
- Visualizar como os valores retornam na “pilha de chamadas”.

---

## 🧠 Explicação do raciocínio  
A função `fatorial` funciona da seguinte forma:

- Se `n` é `0` ou `1`, retorna **1** (caso base).  
- Caso contrário, retorna `n * fatorial(n - 1)`.

Isso causa chamadas recursivas até chegar ao caso base, e depois os valores começam a retornar em ordem inversa, formando o resultado final.

---

## 🔍 Rastreamento passo a passo (fatorial 4)

Chamando:

`fatorial(4)`

Temos esta sequência:

### ➤ Passo 1  
`fatorial(4)`  
→ retorna `4 * fatorial(3)`

### ➤ Passo 2  
`fatorial(3)`  
→ retorna `3 * fatorial(2)`

### ➤ Passo 3  
`fatorial(2)`  
→ retorna `2 * fatorial(1)`

### ➤ Passo 4 – Caso base  
`fatorial(1)`  
→ retorna `1`

Agora, a pilha de chamadas retorna os valores:

- `fatorial(1)` → 1  
- `fatorial(2)` → 2 * 1 = 2  
- `fatorial(3)` → 3 * 2 = 6  
- `fatorial(4)` → 4 * 6 = 24  

### ✔️ Resultado final  

`24`

---

## 🚀 Código da solução
O código completo está disponível em **[solucao.py](./solucao.py)**

---

## 🖥 Exemplo de execução

```text
calculando o fatorial de 4
calculando o fatorial de 3
calculando o fatorial de 2
calculando o fatorial de 1
fatorial de 1 = 1
fatorial de 2 = 2
fatorial de 3 = 6
fatorial de 4 = 24
24
```

---

## 📚 Aprendizado

- Como funciona a recursão usando chamadas que dependem de chamadas menores.
- A importância do caso base para evitar recursão infinita.
- Como funciona a pilha de chamadas (stack).
- Diferença entre processo de chamada e processo de retorno.
- Como acompanhar visualmente a execução recursiva usando print().