#Debemos pedirle al usuario 3 datos: su nombre, una capital y un color.

# Con los dos últimos valores, crearemos el nombre para una cervecería artesanal.

#Vamos a solicitarle el nombre al usuario:
nombre = input("Ingresá tu nombre: ")
#vamos a solicitarle al usuario que ingrese la primer palabra:
capital = input("Ingresá el nombre de tu capital favorita: ")
#vamos a solicitarle al usuario que ingrese la segunda palabra:
color = input("Ingresá el nombre de tu color favorito: ")
#imprimimos en pantalla la concatenación de ambas variables para formar el nombre de la cervecería:
print(f"{nombre}, el nombre de la cervecería artesanal es {capital} {color}.")