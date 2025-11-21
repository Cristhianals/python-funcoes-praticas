import types
def imprime_lista(l,espaço=""):
    try:
        for x in l:
            if isinstance(x, list):
                print("Entrando em:", x)
                imprime_lista(x,espaço + "   ")
                print("Saindo da sublista:", x)
            else:
                print(espaço,x)
    except Exception:
       raise print("algo de errado nao esta certo") from None
    else:
        print("deu tudo certo")
    finally:
        print("sempre sera executadado")
l = [1,[2,3,4,[5,6,7]]]
imprime_lista(l)
