def validacao(a,b,c):#usado apenas uma veriavel com todas as opcoes validas, dps fazer um for
    a,b,c = a.lower(),b.lower(),c.lower()
    while True:
        #a,b,c = a.lower(),b.lower(),c.lower()
        #print("as opcoes validades sao,{0:}{1:}{2:}".format(a,b,c))
        entrada = input("digite uma letra").lower()
        if entrada == a or entrada == b or entrada == c:
            #return "({0:}) é uma opcaovalida".format(entrada)
            return entrada
        else:
            print("({0:}) nao é uma opcao valida!".format(entrada))
print(validacao("a","z","x"))
