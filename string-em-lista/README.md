# 🧩 Função Verifica String em Lista

## 📋 Enunciado  

Escreva uma função que receba uma **string** e uma **lista**, e verifique se essa string está presente dentro da lista.  
A função deve retornar:  
- **True** → se a string estiver na lista  
- **False** → caso contrário

---

## 🎯 Objetivo do exercício  

- Aprender a verificar a existência de elementos em listas.  
- Utilizar o operador `in`, muito importante em Python.  
- Trabalhar com funções simples, objetivas e reutilizáveis.  
- Reforçar comparação entre strings.

---

## 🧠 Explicação do raciocínio  

A lógica é simples:  
Python permite verificar rapidamente se um valor está em uma lista usando o operador `in`.

Exemplo:  
```python
"banana" in ["banana", "uva", "maçã"]  # True
```

A função apenas retorna esse resultado, tornando o código limpo e direto ao ponto.

Esse tipo de verificação é muito comum em:
- buscas
- filtros
- menus
- sistemas de login
- validação de opções

---

## 🚀 Código da solução  

O código completo está disponível em **[string-em-lista.py](./string-em-lista.py)**.

---

## 🖨 Exemplo de execução

```python
print(string_lista("fruta",l))
False
print(string_lista("trufa",l))
False
```

---

## 📚 Aprendizado

- Como usar o operador in para pesquisar valores em listas.
- Diferença entre escrever "fruta" e "frutas" (a comparação é literal).
- Como retornar valores booleanos diretamente sem usar if.
- Como funções simples podem resolver verificações comuns.
- Como listas armazenam valores e permitem buscas eficientes.