
def removeElem(m,i): # Quita el i-esimo elemento del arreglo m y retorna el arreglo final
    del m[i]
    return m


def darCambio(M, i, n, resto, monedas):
    if resto == 0:
        return monedas
    elif i == 1:
        return n//M[1]
    else:
        if n in M:
            return 1
        else:
            return min(darCambio(removeElem(M,i-1), n, n%M[i], monedas+n//M[i]), darCambio(removeElem(M,i-1), n, n%M[i], monedas+n//M[i]))
        





n = int(input("Por favor ingresar valor n: "))
while n < 0 or type(n) != int:
    n = int(input("Valor invalido ingresado por favor reintentar.\n"))

m = int(input("Por favor ingresar valor m: "))
while type(m) != int:
    m = int(input("Valor invalido ingresado por favor reintentar.\n"))

M = []
for i in range(0,m):
    print("Por favor ingresar denominacion de la moneda ",i+1,":")
    M.append(int(input()))

print(darCambio(M, m, n, -1, 0))