from re import I

lista = [1,8,26,4,2,9,45,33,52,11,18,13]

#En base a la lista informada:

#Crear una lista llamada "Par", agregando de la lista original los números pares
#Crear una lista llamada "Impar", agregando de la lista original los números impares
#Imprimir la cantidad y la suma de elementos de la lista inicial

#Creamos listas vacías que almacenarán los distintos números
Par = []
Impar = []

#Realizamos la iteración de los elementos en 'lista'
for x in lista:
    if x % 2 == 0:
        Par.append(x) #si el módulo del elemento iterado es igual a 0, el mismo se almacenará en la lista llamada 'Par'
    else:
        Impar.append(x) #si el módulo del elemento iterado es distinto a 0, el mismo se almacenará en la lista llamada 'Impar'

print(Par) #mostramos los elementos de la lista 'Par'
print(Impar) #mostramos los elementos de la lista 'Impar'

print(len(lista)) #imprimimos la cantidad de elementos dentro de 'lista' con la función '.len'

i = 0 #declaramos la variable 'i' en '0' para poder almacenar allí los elementos iterados

for a in lista: #iteramos los elementos de 'lista'
    i += a #en la variable 'i' vamos almacenando y sumando entre sí los valores que se encuentran dentro de 'lista'

print(i) #nos muestra el resultado de la variable 'i', que responde a la suma total de los elementos dentro de la variable 'lista'