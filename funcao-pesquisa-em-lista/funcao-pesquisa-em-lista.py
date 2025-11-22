#usando find
def pesquisa(l,valor):
    resultado = []
    for i,x in enumerate(l):
        p = 0
        while p > -1:
            p = x.find(valor,p)
            if p >=0:
                resultado.append(f"l[{i}][{p}]")
                p +=1
    if not resultado == []:
        return f"{valor} foi encontrado nas posicoes: " + ",".join(resultado)
    else:
        return f"{valor} nao foi encontrado"
l=["o rato","roeu","a roupa","do rei","de reoma"]
print(pesquisa(l,"r"))
#usando in
def pesquisas(l,valor):
    return valor in l 
l=[20,30,55,84,1,51]
print(pesquisas(l,20))          
