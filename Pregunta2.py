# sum = valor t a sumar
# x = valor necesario para sumar 'sum'
# y = size de la lista L
# z = lista L
# para funcion resultado: x = t, y = n, L = z

def iteracion(sum,x,y,z):
    i = 0
    while i != y:
        if (z[i] == sum):       # Si el número en L[i] es directamente el valor t (no hay recursión)
            cand.append([sum])

        elif (z[i] == x):       # Si el número en L[i] suma el número buscando (final de la recursión)
            return [x]



        elif (z[i] < x):        # Si el número no alcanza a sumar el número buscado (se inicia recursión)
            if (i+1 != y):
                temp1 = iteracion(sum,x-z[i],y-i-1,z[i+1:]) # -1 o [algo]
                if (temp1 != -1): # Si no es -1 significa que encontró una suma
                    temp2 = [z[i]] + temp1
                    if (x != sum): # Evitar que retorne
                        return temp2
                    else: cand.append(temp2)
        i+=1

    return -1

def resultado(sum,t,n,L):
    print('')
    iteracion(sum,t,n,L)
    if (len(cand) > 0):
        new_cand = []
        for elem in cand: # Eliminar repetidos
            if elem not in new_cand:
                new_cand.append(elem)

        print('Suma de '+str(sum)+':') # Imprimir
        for elem1 in new_cand:
            string = ''
            for elem_ in elem1:
                string += str(elem_)
                string += '+'
            print(string[:-1])
    else:
        print('Suma de '+str(sum)+':')
        print('NADA')


rep = int(input("Ingrese número de casos de prueba: "))  # ENTRADAS
entradas = [] # Lista de listas
i = 0
while i < rep:
    entrada = [] # Lista con t, n, L
    entrada.append(int(input('Ingrese t: '))) # t
    tmp = int(input('Ingrese n: ')) # n
    entrada.append(tmp)
    j = 0
    tempL = []
    while j < tmp:
        tempL.append(int(input('Ingrese valor entero: '))) # X_i
        j+=1
    entrada.append(tempL)
    entradas.append(entrada)
    i+=1

for caso in entradas:
    cand = []
    resultado(caso[0],caso[0],caso[1],caso[2])
