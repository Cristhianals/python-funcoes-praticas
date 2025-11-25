# 🔡 Função de Validação de Opções (com Input)

## 📋 Enunciado  

Escreva uma função que receba **três letras** representando opções válidas.  
A função deve:

1. Converter todas as opções válidas para **minúsculas**.  
2. Ler uma letra digitada pelo usuário usando `input()`.  
3. Converter a entrada também para **minúsculas**.  
4. Verificar se a letra digitada está entre as opções válidas.  
5. Caso seja inválida, pedir novamente até que o usuário digite uma opção correta.

A função deve **retornar a opção válida escolhida pelo usuário**.

---

## 🎯 Objetivo do exercício  

- Praticar conversão de dados (`lower()`).  
- Utilizar `input()` dentro de loops.  
- Treinar validação de entradas.  
- Reforçar comparações entre strings.  
- Controlar fluxo com `while True`.  
- Desenvolver lógica de repetição até entrada ser válida.

---

## 🧠 Explicação do raciocínio  

1. As opções válidas são convertidas para minúsculas para evitar erros quando o usuário digita maiúsculas ou minúsculas.  
2. Dentro de um loop infinito (`while True`), a função pede que o usuário digite uma letra.  
3. A entrada é convertida para minúsculas e comparada com as opções válidas.  
4. Se for válida, o loop é encerrado e o valor é retornado.  
5. Se for inválida, a função informa o usuário e continua pedindo nova entrada.

Esse tipo de função é muito comum em:  
- menus  
- sistemas de opções  
- formulários de terminal  
- validação de comandos simples

---

## 🚀 Código da solução  

O código completo está disponível em **[validacao-opcoes-input.py](./validacao-opcoes-input.py)**

## 🖨 Exemplo de execução

```text
Digite uma letra: P
(p) não é uma opção válida!
Digite uma letra: X

x

```

---

## 📚 Aprendizado

- Como usar input() dentro de funções interativas.
- Como usar lower() para padronizar entradas.
- A lógica do while True + return como forma simples de validação.
- Organização de múltiplas opções válidas.
- Diferença entre comparar strings diretamente (a == b) e usar listas/tuplas.
- Como estruturar repetições até o usuário fornecer um valor correto.

---

## 🔧 Extras: Melhorias e Variações Possíveis

- Permitir qualquer quantidade de opções, usando lista ou string:
```python
if entrada in opcoes:
    return entrada

```