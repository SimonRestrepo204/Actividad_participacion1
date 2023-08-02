lista1 = [1, 2, 3, 5, 6]

def mayor(lista1):
    max = lista1[0];
    for x in lista1:
        if x > max:
            max = x
    return max    
 
def menor(lista1):
    min = lista1[0];
    for x in lista1:
        if x < min:
            min = x
    return min
 
def main(lista1):

    print ("El número mayor de la lista es ", mayor(lista1))
    print ("El número menor de la lista es ", menor(lista1))
main(lista1)
