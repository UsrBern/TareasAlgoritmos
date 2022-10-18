
def removeElem(m,i): # Quita el i-esimo elemento del arreglo m y retorna el arreglo final
    del m[i]
    return m


# darCambio(M,i,n,resto,monedas): funcion de recursion
# M: Arreglo con los tipos de monedas
# n: el cambio a dar
# i: Largo del arreglo
# resto: N%M[i], se usa para la recursion
# monedas: cantidad de monedas requeridas para pagar el cambio n

def darCambio(M, n, resto, monedas):
    i = len(M)
    if resto == 0: # si no hay resto, significa que se tiene una cantidad de monedas que puede pagar el cambip
        return monedas
    elif i == 1: # si solo hay un tipo de moneda, la cantidad de monedas requeridas es la division entera del cambio por el tipo de moneda
        return n//M[0]
    else:
        if n in M: # si hay una moneda con el mismo valor del cambio entonces solo se requiere una moneda para pagarlo
            return 1
        else: # recursion
            return min(darCambio(removeElem(M,i-2), n, n%M[i-1], monedas+n//M[i-1]), # el ultimo tipo requiere menos monedas
                       darCambio(M[:i-1], n, n%M[i-2], monedas+n//M[i-2])) # el penultimo tipo requiere menos monedas
        





n = int(input())
while n < 0 or type(n) != int:
    n = int(input("Valor invalido ingresado por favor reintentar.\n"))

m = int(input())
while type(m) != int:
    m = int(input("Valor invalido ingresado por favor reintentar.\n"))

M = []
for i in range(0,m):
    M.append(int(input()))

print(darCambio(M, n, 1, 0))