sum = 6 # Número buscado
n = 8 # Cantidad de elementos en la lista
lis = [6,4,3,3,3,2,2,2] # Lista L
cand = [] # Vacía

def asd(x,y,z):
    i = 0
    while i != y:
        if (z[i] == sum):       # Si el número en L[i] es la suma (no hay recursión)
            cand.append([sum])

        elif (z[i] == x):       # Si el número en L[i] suma el número buscando (final de la recursión)
            return [x]



        elif (z[i] < x):        # Si el número no alcanza a sumar el número buscado (se inicia recursión)
            if (i+1 != y):
                temp1 = asd(x-z[i],y-i-1,z[i+1:]) # -1 o [algo]
                if (temp1 != -1): # Si no es -1 significa que encontró una suma
                    temp2 = [z[i]] + temp1
                    if (x != sum): # Evitar que retorne
                        return temp2
                    else: cand.append(temp2)
        i+=1

    return -1
asd(sum,n,lis)
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