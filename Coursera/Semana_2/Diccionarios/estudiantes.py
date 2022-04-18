# Retomemos el ejemplo de los diccionarios que representan los estudiantes de la universidad. Cada estudiante tendrá un
# nombre, código, género, carrera, promedio y semestre según créditos. Estas características son las que nos permiten
# definir las claves o llaves que podemos ver en el diccionario de ejemplo. Todos los diccionarios que representen
# estudiantes tendrán la misma estructura, es decir, las mismas claves. Pasemos, ahora sí, a nuestros ejercicios.
# Vamos a crear tres funciones sobre grupos de cuatro estudiantes, cada uno representado por uno de los diccionarios
# que vimos anteriormente. Empecemos con nuestra primera función. Debemos crear una función llamada buscar_estudiante
# que recibe los cuatro diccionarios que representan los estudiantes y un string que corresponde al nombre
# de un estudiante. La función debe retornar el diccionario del estudiante cuyo nombre es idéntico al dado por el
# parámetro o None, en caso de que ninguno de los estudiantes tenga dicho nombre. Se nos solicita asímismo crear
# el programa principal que nos permita ejecutar la función. Pasemos a Spider y veamos la solución. Tenemos nuestra
# función buscar_estudiante, que recibe como parámetro los cuatro diccionarios y el nombre. Vamos a empezar creando
# una variable en la que almacenaremos el diccionario del estudiante buscado, en caso de que exista. Lo llamaremos
# buscado y tendrá el valor None inicialmente, teniendo en cuenta que este es el valor a retornar en caso de que no
# se encuentre un estudiante con el nombre dado por parámetro.


# def crea_estudiante() -> list:

estudiantes = []
estudiante = {
        'nombre': '',
        'codigo': 0,
        'genero': '',
        'carrera': '',
        'promedio': 0,
        'scc': ''
    }
for i in range(4):
    estudiante['nombre'] = input('Ingrese el nombre del estudiante n°', i + 1)
    estudiante['codigo'] = int(input('Ingrese el código del estudiante n°', i + 1))
    estudiante['genero'] = input('Ingrese el genero del estudiante n°', i + 1)
    estudiante['carrera'] = input('Ingrese la carrera del estudiante n°', i + 1)
    estudiante['promedio'] = float(input('Ingrese el promedio del estudiante n°', i + 1))
    estudiante['ssc'] = input('Ingrese el ssc del estudiante n°', i + 1)
    estudiantes.append(estudiante)

print(estudiantes)
