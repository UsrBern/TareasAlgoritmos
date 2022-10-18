sum = 6
n = 8 # Cantidad de elementos en la lista
lis = [6,4,3,3,3,2,2,2] # Lista L
cand = [] #vacía

def asd(x,y,z):
    i = 0
    while i != y:
        if (z[i] == sum):
            cand.append([sum])

        elif (z[i] == x):
            return [x]



        elif (z[i] < x):
            if (i+1 != y):
                temp1 = asd(x-z[i],y-i-1,z[i+1:]) # -1 o [algo]
                if (temp1 != -1):
                    temp2 = [z[i]] + temp1
                    if (x != sum):
                        return temp2
                    else: cand.append(temp2)
        i+=1

    return -1
asd(sum,n,lis)

new_cand = []
for elem in cand: # Eliminar repetidos
    if elem not in new_cand:
        new_cand.append(elem)
print(new_cand)


