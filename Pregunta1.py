
# darCambio(n, M, monedas): funcion de recursion
# n: el cambio a dar
# M: Arreglo con los tipos de monedas
# monedas: cantidad de monedas acumuladas hasta ahora, valor inicial = 0

def darCambio(n, M, monedas):
    i = len(M)-1
    if n == 0 or len(M) == 0: # Si no hay vuelto o no hay monedas se retornan las monedas acumuladas hasta ahora
        return monedas
    elif n == 1: # Si el vuelto es 1, se paga con una moneda de 1
        return 1
    else:
        if n%M[i] == 0: # Si el n%=M[i], la cantidad de monedas necesarias para pagar n es n//M[i]
            return monedas+n//M[i]
        else: # recursion, se toma el camino que resulte en la menor cantidad de monedas requeridas
            return min(
                darCambio(n-M[i]*(n//M[i]), M[:i], monedas+n//M[i]),
                darCambio(n-M[i-1]*(n//M[i-1]), M[:i-1], monedas+n//M[i-1])
            )



# MAIN

n = int(input())
while n < 0 or type(n) != int:
    n = int(input("Valor invalido ingresado por favor reintentar.\n"))

m = int(input())
while type(m) != int:
    m = int(input("Valor invalido ingresado por favor reintentar.\n"))

M = []
for i in range(0,m):
    M.append(int(input()))

print(darCambio(n,M,0))