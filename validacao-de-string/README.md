# 🔤 Função de Validação de String

## 📋 Enunciado  

Escreva uma função que valide uma string com base em seu tamanho.  
A função deve receber:  
- a **string** a ser validada  
- o **tamanho mínimo** permitido  
- o **tamanho máximo** permitido  

A função deve retornar **True** se a string estiver dentro do intervalo permitido, e **False** caso contrário.

---

## 🎯 Objetivo do exercício  

- Praticar validação de dados em funções.  
- Aprender a usar `len()` para medir o tamanho de strings.  
- Aplicar operadores lógicos (`and`, `or`, `<`, `>`, `<=`, `>=`).  
- Criar funções que trabalham com regras e limites definidos pelo usuário.

---

## 🧠 Explicação do raciocínio  

A função simplesmente compara o tamanho da string com os valores mínimo e máximo informados.  

O raciocínio é:  
- Se o comprimento da string (`len(string)`) for maior ou igual ao **mínimo**  
  **e**  
  menor ou igual ao **máximo**, então a string é válida.  
- Caso contrário, retorna `False`.

É uma função de validação muito comum em cadastro de usuários, validação de entrada de dados e sistemas de formulário.

---

## 🚀 Código da solução  

O código completo está disponível em **[validacao-de-string.py](./validacao-de-string.py)**

---

## 🖨 Exemplo de execução

```python
valida_string("python", 10, 3) → True  
valida_string("oi", 5, 3) → False  
valida_string("desenvolvimento", 12, 3) → False
```

---

## 📚 Aprendizado

- Como medir o tamanho de uma string usando len().
- Como comparar valores usando operadores lógicos.
- Como criar funções de validação simples e reutilizáveis.
- Como trabalhar com limites mínimo e máximo.
- Como estruturar condições com clareza e boa legibilidade.