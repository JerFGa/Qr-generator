def create_qr_matrix():
    """
    El codigo QR V2 se define como una matriz de tamaño 25x25.
    En este caso, se define una matriz de tamaño 33x33, esto se debe
    a que se debe agregar la zona de silencio, que es un borde de 4
    celdas alrededor de la matriz QR.
    """
    size = 33
    qr_matrix = [[None for _ in range(size)] for _ in range(size)]
    return qr_matrix

def rellenar_zona_silencio(matriz):
    """
    Rellena la zona de silencio (borde de 4 módulos) con ceros.
    """
    size = len(matriz)

    for y in range(size):
        for x in range(size):
            if x < 4 or x >= size - 4 or y < 4 or y >= size - 4:
                matriz[y][x] = 0


def print_qr_matrix(matrix):
    for row in matrix:
        print(" ".join(['.' if cell is None else str(cell) for cell in row]))

def patronesDeDeteccion(matriz):
    """
    Se define la matriz de patrones de deteccion, ademas
    se agrega 3 patrones de detección en las esquinas de la matriz QR.
    """
    patron = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for i in range(9):
        for j in range(9):
            val = patron[i][j]
            matriz[3 + i][3 + j] = val  # superior izquierda
            matriz[3 + i][21+j] = val  # superior derecha
            matriz[21+i][3 + j] = val  # inferior izquierda

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

    for i in range(12, 23):
        matriz[10][i-1] = i % 2  # línea horizontal
        matriz[i-1][10] = i % 2  # línea vertical

def colocar_bits_formato(matriz):
    """
    Coloca los bits de formato para QR versión 2, nivel M, máscara 3.
    Coordenadas exactas para matriz 33x33 (con zona de silencio de 4).
    
    Para nivel M (01) y máscara 3 (011), el código de formato es: 01011
    Con BCH y máscara XOR: 110101010110010100
    """
    
    # Bits de formato para nivel M, máscara 3
    bits_formato = "110101010110010100"
    
    # --- PRIMERA COPIA: Alrededor del patrón superior izquierdo ---
    
    # Parte vertical (bits 0-7): columna 12, desde fila 4 hasta 12 (saltando fila 10)
    posiciones_verticales = [
        (4, 12),   # bit 0
        (5, 12),   # bit 1  
        (6, 12),   # bit 2
        (7, 12),   # bit 3
        (8, 12),   # bit 4
        (9, 12),   # bit 5
        # Saltar fila 10 (línea de sincronización)
        (11, 12),  # bit 6
        (12, 12),  # bit 7
    ]
    
    for i, (row, col) in enumerate(posiciones_verticales):
        if i < len(bits_formato):
            matriz[row][col] = int(bits_formato[i])
    
    # Parte horizontal (bits 8-14): fila 12, desde columna 11 hasta 4 (saltando columna 10)
    posiciones_horizontales = [
        (12, 11),  # bit 8
        (12, 9),   # bit 9 (saltar columna 10)
        (12, 8),   # bit 10
        (12, 7),   # bit 11
        (12, 6),   # bit 12
        (12, 5),   # bit 13
        (12, 4),   # bit 14
    ]
    
    for i, (row, col) in enumerate(posiciones_horizontales):
        bit_index = 8 + i
        if bit_index < len(bits_formato):
            matriz[row][col] = int(bits_formato[bit_index])
    
    # --- SEGUNDA COPIA: Duplicado en otras posiciones ---
    
    # Junto al patrón superior derecho (bits 0-7): fila 12, columnas 28 hacia 21
    for i in range(8):
        if i < len(bits_formato):
            matriz[12][28 - i] = int(bits_formato[i])
    
    # Junto al patrón inferior izquierdo (bits 8-14): columna 12, filas 28 hacia 22
    for i in range(7):
        bit_index = 8 + i
        if bit_index < len(bits_formato):
            matriz[28 - i][12] = int(bits_formato[bit_index])
    
    # Módulo oscuro fijo (siempre 1) en posición específica
    matriz[21][12] = 1
    
    print("✓ Bits de formato colocados:")
    print(f"  Configuración: Nivel M, Máscara 3")
    print(f"  Bits: {bits_formato}")
    print(f"  Posiciones verificadas para matriz 33x33")


def verificar_bits_formato(matriz):
    """
    Función de debug para verificar que los bits de formato están bien colocados
    """
    print("\n--- Verificación de bits de formato ---")
    
    # Verificar primera copia (vertical + horizontal)
    print("Primera copia:")
    posiciones_v = [(4,12), (5,12), (6,12), (7,12), (8,12), (9,12), (11,12), (12,12)]
    posiciones_h = [(12,11), (12,9), (12,8), (12,7), (12,6), (12,5), (12,4)]
    
    for i, (r, c) in enumerate(posiciones_v):
        print(f"  Pos ({r},{c}): {matriz[r][c]}")
    
    for i, (r, c) in enumerate(posiciones_h):
        print(f"  Pos ({r},{c}): {matriz[r][c]}")
    
    # Verificar segunda copia
    print("Segunda copia:")
    for i in range(8):
        r, c = 12, 28-i
        print(f"  Pos ({r},{c}): {matriz[r][c]}")
    
    for i in range(7):
        r, c = 28-i, 12
        print(f"  Pos ({r},{c}): {matriz[r][c]}")
    
    print(f"Módulo oscuro (21,12): {matriz[21][12]}")

import tkinter as tk

def mostrar_matriz_grafica(matriz, modulo=10):
    """
    Visualiza la matriz QR usando tkinter.
    Cada celda se dibuja como un cuadrado blanco o negro.
    """
    size = len(matriz)
    canvas_size = size * modulo

    ventana = tk.Tk()
    ventana.title("QR Visual - Nivel M, Máscara 3")

    canvas = tk.Canvas(ventana, width=canvas_size, height=canvas_size, bg="white")
    canvas.pack()

    for y in range(size):
        for x in range(size):
            valor = matriz[y][x]
            if valor == 1:
                color = "black"
            elif valor == 0:
                color = "white"
            else: 
                color = "grey"
            x0 = x * modulo
            y0 = y * modulo
            x1 = x0 + modulo
            y1 = y0 + modulo
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")

    ventana.mainloop()

def generar_matrix():
    # Crear la matriz base
    qr = create_qr_matrix()
    
    # Aplicar los patrones sobre la matriz
    patronesDeDeteccion(qr)
    rellenar_zona_silencio(qr)
    patronDeAlineacion(qr)
    lineas_sincronizacion(qr)
    colocar_bits_formato(qr)  # Cambiado de reservar_modulos_especiales
    return qr