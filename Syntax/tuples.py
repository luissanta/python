names = ('luis', 'fernando')
mix = (2, 'luis', True)

print(mix[0:2])     # primer valor: inicio - segundo valor: fin(sin tomarlo)


# Modificar tuplas
list = list(mix)    # Conertir a lista
list[0] = 9         # Modificar
mix = tuple(list)   # Convertir a tupla

print(mix)
