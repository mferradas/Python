''' EJERCICIO:

- La función de palabra_más_larga se usa para comparar 3 palabras. 
- Debe devolver la palabra con mayor número de caracteres (y la primera de la lista cuando tienen la misma longitud). 
- Complete el espacio en blanco para que esto suceda.

'''

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3): # la primera de la lista...
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))