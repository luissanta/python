# Escriba una función que cuente la cantidad de caracteres diferentes que aparecen más de una vez en una cadena.
#
# Suponga que todas las cadenas se componen únicamente de letras minúsculas del alfabeto en inglés.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: contar_caracteres_repetidos
# Si lo requiere, puede agregar funciones adicionales.


def contar_caracteres_repetidos(frase_a_analizar: str) -> int:
    caracteres_repetidos = 0
    letras = {}
    for i in frase_a_analizar:
        if i not in letras:
            letras[i] = 1
        else:
            if letras[i] <= 1:
                caracteres_repetidos += 1
            letras[i] += 1
    return caracteres_repetidos


frase = input('Ingrese una frase: ')
print(contar_caracteres_repetidos(frase))
