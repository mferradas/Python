'''
EJERCICIO:

- Complete el cuerpo de la función format_name. 
- Esta función recibe los parámetros first_name y last_name y luego devuelve una cadena con el formato adecuado.
- Específicamente:

- Si se proporcionan los parámetros last_name y first_name, la función debería regresar lo siguiente:

print(format_name("Ella", "Fitzgerald"))
Name: Fitzgerald, Ella

- Si solo se proporciona un parámetro de nombre (ya sea el nombre o el apellido), la función debería devolverse así:

print(format_name("Adele", ""))
Name: Adele

- O:

print(format_name("", "Einstein"))
Name: Einstein

- Finalmente, si ambos nombres están en blanco, la función debería devolver la cadena vacía:

print(format_name("", ""))

'''

def format_name(first_name, last_name):

    if first_name == '' and last_name == '':
        return('')
    elif first_name == '':
        return('Name: '+last_name)
    elif last_name == '':
        return('Name: '+first_name)
    elif first_name != '' and last_name != '':
        return('Name: ' + last_name + ', ' + first_name)    
	
print(format_name("Ernest", "Hemingway")) # Should return the string "Name: Hemingway, Ernest"
print(format_name("", "Madonna")) # Should return the string "Name: Madonna"
print(format_name("Voltaire", "")) # Should return the string "Name: Voltaire"
print(format_name("", "")) # Should return an empty string
