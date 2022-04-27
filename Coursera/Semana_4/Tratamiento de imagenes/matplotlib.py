# noinspection PyUnresolvedReferences
import matplotlib.image as mpimg
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt


def cargar_imagen_matriz(ruta_imagen: str) -> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz de MxNx3
    """
    imagen = mpimg.imread(ruta_imagen)
    return imagen


def convertir_a_grises(imagen_a_convertir: list) -> None:
    alto = len(imagen_a_convertir)
    ancho = len(imagen_a_convertir[0])
    for i in range(0, alto):
        for j in range(0, ancho):
            rojo, verde, azul = imagen_a_convertir[i][j]
            gris = (rojo + verde + azul) // 3
            imagen_a_convertir[i][j] = (gris, gris, gris)


def convertir_a_binario(imagen: list, umbral: int) -> None:
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(0, alto):
        for j in range(0, ancho):
            rojo, verde, azul = imagen[i][j]
            gris = (rojo + verde + azul) // 3
            if gris < umbral:
                imagen[i][j] = (0, 0, 0)
            else:
                imagen[i][j] = (255, 255, 255)


def visualizar_imagen_matriz(imagen: list) -> None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list): Matriz de MxNx3 que representa la imagen a visualizar.
    """
    plt.imshow(imagen)
    plt.show()


imagen_muestra = cargar_imagen_matriz("muestra.jpg")
convertir_a_grises(imagen_muestra)
visualizar_imagen_matriz(imagen_muestra)
