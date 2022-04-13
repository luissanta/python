# Considere el software que se ejecuta en una máquina expendedora.
# Una de las tareas que debe realizar es determinar cuánto cambio debe
# entregarle al cliente luego de que paga. Escriba una función que recibe la cantidad de dinero
# (en pesos) a dar como cambio al cliente y retorne un mensaje con la cantidad de monedas
# de cada denominación que deben ser entregadas, teniendo en cuenta que el cambio se debe
# otorgar con la menor cantidad de monedas posible.
#
# La máquina cuenta con monedas de 500, 200, 100 y 50 pesos, y el cambio total se entregará
# con monedas de estas denominaciones. El mensaje retornado DEBE seguir el siguiente formato:
# “A,B,C,D” (sin espacios intermedios) donde A, B, C y D son la cantidad de monedas de
# 500, 200, 100 y 50, respectivamente.
#
# Su solución debe tener una función de acuerdo con la siguiente especificación:
#
# Nombre de la función: calcular_cambio
#
# Si lo requiere, puede agregar funciones adicionales.


def change_to_return(money: int) -> str:
    coins_500, residue = divmod(money, 500)
    coins_200, residue = divmod(residue, 200)
    coins_100, residue = divmod(residue, 100)
    coins_50, residue = divmod(residue, 50)
    return str(coins_500) + ',' + str(coins_200) + ',' + str(coins_100) + ',' + str(coins_50)


m = int(input('Ingrese cambio a retornar: '))

print(change_to_return(m))
