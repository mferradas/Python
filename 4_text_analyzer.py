'''
PROYECTO: ANALIZADOR DE TEXTO
* * * CONSIGNA * * *
* * 1) Pedirle al usuario que ingrese un texto (frase, poema, párrafo, oración)
* * 2) Pedirle al usuario que ingrese 3 letras a su elección
* * 3) El programa deberá devolver la siguiente información:
A) Cuántas veces aparece cada una de las letras que el usuario eligió
B) Cuántas palabras hay a lo largo de todo el texto (total)
C) Primera y última letra del texto
D) Colocar las  palabras en orden inverso
E) Verificar si la palabra 'Python' se encuentra en el texto
'''
#le pedimos al usuario que ingrese un texto de su preferencia
texto = input("Ingrese un texto: ")

#pasamos el texto a minúsculas para efectuar la comparación con las letras que deberá ingresar el usuario
textoEnMinusculas = texto.lower()

#generamos un espacio
print("")

#LETRA 1
#pedimos al usuario que ingrese la primer letra
letra1 = input("Ingrese una primer letra: ")
#pasamos el dato ingresado a minúscula
letra1EnMinusculas = letra1.lower()

#LETRA 2
#pedimos al usuario que ingrese la segunda letra
letra2 = input("Ingrese una segunda letra: ")
#pasamos el dato ingresado a minúscula
letra2EnMinusculas = letra2.lower()

#LETRA 3
#pedimos al usuario que ingrese la tercera letra
letra3 = input("Ingrese una tercer letra: ")
#pasamos el dato ingresado a minúscula
letra3EnMinusculas = letra3.lower()

#generamos un espacio
print("")

#crear lista con las letras ingresadas
lista_letras = [letra1.lower(), letra2.lower(), letra3.lower()]

#mostrar las letras ingresadas por el usuario
print(f"Las letras ingresadas son: {lista_letras}.")

#generamos un espacio
print("")

#convertimos los elementos de 'texto' a una lista
texto_list = textoEnMinusculas.split()

#imprimimos la cantidad de elementos de la lista (cantidad de palabras del texto)
print("El texto tiene",len(texto_list),"palabras.")

#generamos un espacio
print("")

buscarLetra1 = textoEnMinusculas.count(letra1EnMinusculas) #buscamos y contamosla letra 1 en el texto
buscarLetra2 = textoEnMinusculas.count(letra2EnMinusculas) #buscamos y contamos la letra 2 en el texto
buscarLetra3 = textoEnMinusculas.count(letra3EnMinusculas) #buscamos y contamos la letra 3 en el texto

print(f"La letra {letra1EnMinusculas} se encuentra {buscarLetra1} veces en el texto.")
print(f"La letra {letra2EnMinusculas} se encuentra {buscarLetra2} veces en el texto.")
print(f"La letra {letra3EnMinusculas} se encuentra {buscarLetra3} veces en el texto.")

primerLetraDelTexto = texto_list[0][0] #última palabra, última letra
ultimaLetraDelTexto = texto_list[-1][-2] #última palabra, última letra

#generamos un espacio
print("")

print(f"La primer letra del texto es la {primerLetraDelTexto} y la última es la {ultimaLetraDelTexto}.")

#generamos un espacio
print("")

textoInverso = texto[::-1] #invertimos el texto
print(textoInverso) #imprimimos el texto invertido

#generamos un espacio
print("")

comprobarPalabra = 'Python' in texto #comprobamos, mediante un bool, si la palabra 'Python' se encuentra dentro del texto

print("")

#
if comprobarPalabra == True:
    print("La palabra 'Python' se encuentra dentro del texto.")
else:
    print("La palabra 'Python' no se encuentra dentro del texto.")

print("")