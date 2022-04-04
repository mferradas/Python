# La función de parte_fraccional divide el numerador por el denominador y devuelve solo la parte fraccionaria (un número entre 0 y 1). 
# Complete el cuerpo de la función para que devuelva el número correcto.
# Nota: Dado que la división por 0 produce un error, si el denominador es 0, la función debería devolver 0 en lugar de intentar la división.

def fractional_part(numerator, denominator):
    
    if denominator == 0:
        return(0)   

    else:
        resultado = numerator / denominator
        n_int = int(resultado)    
        resultado2 = n_int - resultado

    if resultado2 == 0.0:
        return(0)    

    return (abs(resultado2))

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0