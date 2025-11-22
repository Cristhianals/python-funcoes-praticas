# Função Pesquisa em Listas 🔍

## 📝 Enunciado
Escreva uma função que utilize **métodos de pesquisa em lista**, explorando diferentes formas de localizar valores dentro de estruturas de dados.

O exercício deve demonstrar duas abordagens:

1. **Pesquisa dentro de strings contidas em listas**, usando métodos como `.find()`.
2. **Pesquisa direta em listas**, usando o operador `in`.

---

## 🎯 Objetivo do exercício
- Praticar diferentes formas de pesquisa em listas.  
- Entender o uso do método `.find()` para localizar substrings.  
- Utilizar o operador `in` para busca simples dentro de listas.  
- Aprender a combinar `enumerate`, loops e métodos de string para localizar múltiplas ocorrências.  

---

## 🧠 Explicação do raciocínio

### 🔹 Pesquisa com `.find()`
A função `pesquisa(l, valor)` percorre a lista `l`, sendo cada elemento uma string.  
Para cada string, ela usa o método `.find()` repetidamente para localizar **todas as ocorrências** da substring `valor`.

Funcionamento:
- `enumerate(l)` captura o índice da lista e o conteúdo.  
- Dentro do `while`, o método `.find()` procura pela substring começando da posição `p`.  
- Cada ocorrência encontrada é registrada no formato `l[indice][posicao]`.  
- O resultado final exibe TODAS as ocorrências dentro das strings da lista.

### 🔹 Pesquisa com `in`
A segunda versão, `pesquisas(l, valor)`, demonstra o uso direto do operador `in` para verificar se um valor existe dentro de uma lista.

É simples, direta e eficiente — ideal para buscas exatas.

---

## 🚀 Código da solução
O código completo está disponível em [solucao.py](./solucao.py)

---

## 🖨 Exemplo de execução

```text
r foi encontrado nas posicoes: l[0][1],l[1][0],l[3][3]
True
```

## 🧩 **Observacão**: entendendo `l[i][j]`

Isso representa **a localização exata** de cada ocorrência encontrada, usando dois índices:

- `l[i]` → indica **qual string da lista** contém a letra encontrada  
- `l[i][j]` → indica **qual posição dentro dessa string** está a letra

Ou seja:
- **Primeiro índice (`i`)** → posição na lista  
- **Segundo índice (`j`)** → posição dentro da string


isso significa que você pode literalmente digitar esses índices no interpretador Python ou na sua IDE e **acessar exatamente o caractere encontrado**, por exemplo:

```python
print(l[0][2])
print(l[1][0])
print(l[3][3])
```
---

## 📚 Aprendizado

- Uso prático do método .find() para localizar substrings.
- Como usar while para continuar a busca enquanto houver ocorrências.
- Como enumerate() ajuda a rastrear índices da lista durante a busca.
- Construção dinâmica de resultados usando listas e join().
- Uso do operador in para buscas diretas e rápidas em listas.

---

## ✨ Melhorias e variações possíveis

- Ignorar diferenças entre maiúsculas e minúsculas com .lower().
- Permitir buscas completas por palavras usando .split() ou regex.
- Retornar também a quantidade total de ocorrências encontradas.
- Permitir buscar vários valores ao mesmo tempo.
- Criar uma versão otimizada usando algoritmos de busca mais avançados.