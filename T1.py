def darCambio(D, n, num, resto):
    if resto == 0:
        return num
    else:
        divisores = []
        i = 0
        for coin in D:
            divisores.append(n//coin)
            i += 1
        minDiv = min(divisores)
        num += minDiv
        return min(darCambio(D,n,num,num%minDiv), )





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
