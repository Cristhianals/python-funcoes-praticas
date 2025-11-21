'''
def  fibonacci(n):
    x = 2
    fibonaci = [0,1]
    if n == 0 or n == 1:
        return n
    if x == n:
        return fibonaci[x - 1]
    while x <= n:
        fibonaci.append([fibonaci[x-1] + fibonaci[x - 2]])
        x += 1
'''
def fibonacci(n):
    x = 2
    fibonaci = [0,1]
    if n == 0 or n == 1:
        return n
    while x <= n:
        fibonaci.append(fibonaci[0] + fibonaci[1])
        fibonaci.pop(0)
        x += 1
    return fibonaci[1]
print(fibonacci(10))
def fibonaccichatgpt(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def fibonaccigpt2(n):
    if n == 0:
        return 0
    anterior, atual = 0, 1
    for _ in range(2, n + 1):
        proximo = anterior + atual
        anterior = atual
        atual = proximo
    return atual
