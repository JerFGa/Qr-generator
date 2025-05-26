def zigzag(matriz, bitstream):
    """
    Rellena la matriz QR en zigzag con los datos del bitstream.
    Aplica la máscara 3 durante el llenado.
    """
    
    # Dimensiones de la matriz (asumiendo matriz cuadrada)
    size = len(matriz)
    
    # Posición inicial: esquina inferior derecha
    x = size - 1  # columna
    y = size - 1  # fila
    
    # Dirección inicial: hacia arriba
    direction_up = True
    
    # Índice actual en el bitstream
    bit_index = 0

    while x >= 0 and bit_index < len(bitstream):
        # Procesamos la columna actual en la dirección correspondiente
        if direction_up:
            # Subir por la columna
            for row in range(y, -1, -1):
                bit_index = procesar_posicion(matriz, row, x, bitstream, bit_index)

                # También procesamos la columna de la izquierda si existe
                if x - 1 >= 0:
                    bit_index = procesar_posicion(matriz, row, x - 1, bitstream, bit_index)
            y = 0  # Después de subir, estamos en la fila 0
        else:
            # Bajar por la columna
            for row in range(y, size):
                bit_index = procesar_posicion(matriz, row, x, bitstream, bit_index)

                # También procesamos la columna de la izquierda si existe
                if x - 1 >= 0:
                    bit_index = procesar_posicion(matriz, row, x - 1, bitstream, bit_index)
            y = size - 1  # Después de bajar, estamos en la última fila
        
        # Cambiar dirección y moverse a la siguiente columna par
        direction_up = not direction_up
        x -= 2  # Saltamos de columna par a par (o impar a impar)
        
        # Verificar si hemos llegado a la columna de sincronización vertical (columna 6 en QR estándar)
        # En tu matriz de 33x33, esto sería la columna 10 (4 + 6)
        if x == 10:
            x -= 1  # Saltar la columna de sincronización
    
    return matriz


def procesar_posicion(matriz, row, col, bitstream, bit_index):
    """
    Procesa una posición individual en la matriz con datos del bitstream.
    Aplica la máscara 3: (row + col) % 3 == 0
    Retorna el nuevo índice en el bitstream.
    """
    if bit_index >= len(bitstream):
        return bit_index
        
    if matriz[row][col] is None:
        # Usar el bit actual del bitstream
        bit_value = int(bitstream[bit_index])
        
        # Aplicar máscara 3: invertir si (row + col) % 3 == 0
        if (row + col) % 3 == 0:
            bit_value = 1 - bit_value  # Invertir el bit
        
        matriz[row][col] = bit_value
        return bit_index + 1
    else:
        # Posición ocupada, no avanzar en el bitstream
        return bit_index


def aplicar_mascara_completa(matriz):
    """
    Función auxiliar para verificar que la máscara se aplicó correctamente.
    Esta función puede usarse para debuggear.
    """
    size = len(matriz)
    mascara_aplicada = 0
    
    for i in range(size):
        for j in range(size):
            if isinstance(matriz[i][j], int) and (i + j) % 3 == 0:
                # Contar cuántas posiciones fueron afectadas por la máscara
                mascara_aplicada += 1
    
    print(f"Máscara 3 aplicada a {mascara_aplicada} posiciones")
    return mascara_aplicada