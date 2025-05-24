def create_qr_matrix():
    """
    El codigo QR V2 se define como una matriz de tamaño 25x25.
    En este caso, se define una matriz de tamaño 33x33, esto se debe
    a que se debe agregar la zona de silencio, que es un borde de 4
    celdas alrededor de la matriz QR.
    """
    size = 33
    qr_matrix = [[0 for _ in range(size)] for _ in range(size)]
    qr_matrix[28][27] = 1  # Se reserva la celda (29,28) para el formato
    return qr_matrix

def print_qr_matrix(matrix):
    for row in matrix:
        print(" ".join(['.' if cell is None else str(cell) for cell in row]))

def patronesDeDeteccion(matriz):
    """
    Se define la matriz de patrones de deteccion, ademas
    se agrega 3 patrones de detección en las esquinas de la matriz QR.
    """
    patron = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]

    for i in range(7):
        for j in range(7):
            val = patron[i][j]
            matriz[4 + i][4 + j] = val  # superior izquierda
            matriz[4 + i][22+j] = val  # superior derecha
            matriz[22+i][4 + j] = val  # inferior izquierda

def patronDeAlineacion(matriz):

    """ Se define la posicion del patron de alineacion
    en la matriz QR, en este caso se coloca en la posicion (22,22)"""

    patron = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]

    for i in range(5):
        for j in range(5):
            matriz[20+ i][20+j] = patron[i][j]

def lineas_sincronizacion(matriz):

    """
    Coloca las líneas de sincronización en la fila y columna del QR
    que pasa por el centro de los patrones de detección.
    """

    for i in range(12, 22):
        matriz[10][i-1] = i % 2  # línea horizontal
        matriz[i-1][10] = i % 2  # línea vertical

def reservar_modulos_especiales(matriz):
    """
    Reserva los módulos para los bits de formato en la matriz QR.
    Usa 'R' para indicarlos.
    """
    # Formato alrededor del patrón superior izquierdo
    for i in range(9):
        if i != 6:
            matriz[4 + i][12] = 'R'  # Columna a la derecha
            matriz[12][4 + i] = 'R'  # Fila inferior

    # Formato junto al patrón superior derecho
    for i in range(8):         
        matriz[12][28 - i] = 'R'         # Fila horizontal en parte inferior derecha

    # Formato alrededor del patrón inferior izquierdo
    for i in range(7):
            matriz[22+i][12] = 'R'
    matriz[21][12] = 1  # Asi lo construyeron sabra dios por que

import tkinter as tk

def mostrar_matriz_grafica(matriz, modulo=10):
    """
    Visualiza la matriz QR usando tkinter.
    Cada celda se dibuja como un cuadrado blanco o negro.
    """
    size = len(matriz)
    canvas_size = size * modulo

    ventana = tk.Tk()
    ventana.title("QR Visual")

    canvas = tk.Canvas(ventana, width=canvas_size, height=canvas_size, bg="white")
    canvas.pack()

    for y in range(size):
        for x in range(size):
            valor = matriz[y][x]
            if valor == 1:
                color = "black"
            elif valor == 'R':  # Módulos reservados (formato)
                color = "grey"
            else:
                color = "white"
            x0 = x * modulo
            y0 = y * modulo
            x1 = x0 + modulo
            y1 = y0 + modulo
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")

    ventana.mainloop()



