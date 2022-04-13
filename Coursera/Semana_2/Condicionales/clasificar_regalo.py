# En el taller de regalos de Santa Claus, el CTE (Chief Technology Elf)
# ha decidido implementar un nuevo sistema de clasificación de regalos,
# para facilitar su organización. Cada paquete tiene ahora un identificador numérico único.
# El identificador es un número entero entre 100 y 999 y sirve para clasificar los regalos de la siguiente manera.
#
# Si el número es palíndromo e impar, el regalo corresponde a una niña.
#
# Si el número es palíndromo y par, el regalo corresponde a un niño.
#
# Si el número es par pero no es palíndromo, el regalo corresponde a un hombre.
#
# Si el número es impar pero no es palíndromo, el regalo corresponde a una mujer.
#
# Escriba una función que ayude al CTE a calcular, dado un identificador único de regalo,
# a qué tipo de persona corresponde dicho regalo.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
# Nombre de la función: clasificar_regalo
# Si lo requiere, puede agregar funciones adicionales.


def es_palindromo(id_regalo: int) -> bool:
    revert_id_regalo = ''
    for i in str(id_regalo):
        revert_id_regalo = i + revert_id_regalo
    return str(id_regalo) == revert_id_regalo


def es_par(id_regalo: int) -> bool:
    return id_regalo % 2 == 0


def clasificar_regalo(id_regalo: int) -> str:
    own = ''
    if es_par(id_regalo) and es_palindromo(id_regalo):
        own = 'boy'
    elif not es_par(id_regalo) and es_palindromo(id_regalo):
        own = 'girl'
    elif not es_par(id_regalo) and not es_palindromo(id_regalo):
        own = 'woman'
    else:
        own = 'man'
    return own


id_regalo = int(input('Ingrese el id del regalo: '))

print(clasificar_regalo(id_regalo))
