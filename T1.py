def darCambio(D, n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            



n = input("Por favor ingresar valor n: ")
while n < 0 or n is not int:
    n = input("Valor invalido ingresado por favor reintentar.")

m = input("Por favor ingresar valor m: ")
while m is not int:
    m = input ("Valor ingresado invalido por favor reintentar.")

D = []
for i in range(0,m):
    if i == 0:
        D[i] = 1
    else:
        D[i] = input("Por favor ingresar ", i+1, "-esima denominacion de las monedas.")
