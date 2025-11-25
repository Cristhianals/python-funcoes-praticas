# 📚 Função Recursiva para Impressão de Listas com Indentação

## 📋 Enunciado  

Utilizando a função `type` (ou `isinstance`), escreva uma **função recursiva** que imprima os elementos de uma lista.  
Cada elemento deve ser impresso **em uma linha separada**.

Caso existam listas dentro de listas (exemplo:  
`L = [1, [2, 3, 4, [5, 6, 7]]]`), cada nível de profundidade deve ser impresso **mais à direita**, como um bloco indentado em Python.

**Dica:**  
Envie o nível atual como parâmetro e use-o para calcular a quantidade de espaços à esquerda.

---

## 💡 Objetivo do exercício  

- Praticar recursão em Python.  
- Entender o tratamento de listas aninhadas.  
- Usar indentação dinâmica com base no nível atual.  
- Aprender a detectar se um elemento é uma lista usando `isinstance`.  
- Trabalhar com `try / except / else / finally`.

---

## 🧠 Explicação do raciocínio  

A função deve:  
- Percorrer cada elemento da lista.  
- Se o elemento **não for** uma lista → imprime com indentação.  
- Se **for** uma lista → imprime informações de entrada, chama a função novamente aumentando a indentação e, ao final, indica a saída da sublista.  
- A indentação cresce adicionando `"   "` (três espaços) a cada nível.  
- A função também usa `try / except / else / finally` para mostrar o fluxo completo de execução.

---

## 🚀 Código da solução

O código completo está disponível em **[imprime-lista-indentada.py](./imprime-lista-indentada.py)**.

---

## 🖨 Exemplo de execução

```text
 1
Entrando em: [2, 3, 4, [5, 6, 7]]
    2
    3
    4
    Entrando em: [5, 6, 7]
       5
       6
       7
    Saindo da sublista: [5, 6, 7]
Saindo da sublista: [2, 3, 4, [5, 6, 7]]
deu tudo certo
sempre sera executadado
sempre sera executadado

```

---

## 🎯 Aprendizado

- Como percorrer listas recursivamente.
- Como detectar listas internas usando `isinstance(x, list)`.
- Como criar indentação crescente através de parâmetros.
- Uso de `try / except / else / finally` em funções recursivas.
- Como acompanhar o fluxo com mensagens “Entrando em” e “Saindo da sublista”.