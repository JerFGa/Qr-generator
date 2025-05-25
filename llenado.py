def zigzag_patron_ajedrez(matriz, bitstream):
    """
    Rellena la matriz QR en zigzag con los datos del bitstream.
    Si no se proporciona bitstream, genera uno usando encode().
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
    pasos = 0
    max_pasos = size * size * 2  # Límite de seguridad
    
    while x >= 0 and pasos < max_pasos and bit_index < len(bitstream):
        # Procesamos la columna actual en la dirección correspondiente
        if direction_up:
            # Subir por la columna
            for row in range(y, -1, -1):
                bit_index = procesar_posicion(matriz, row, x, bitstream, bit_index)
                pasos += 1
                if pasos >= max_pasos or bit_index >= len(bitstream):
                    break
                # También procesamos la columna de la izquierda si existe
                if x - 1 >= 0:
                    bit_index = procesar_posicion(matriz, row, x - 1, bitstream, bit_index)
                    pasos += 1
                    if pasos >= max_pasos or bit_index >= len(bitstream):
                        break
            y = 0  # Después de subir, estamos en la fila 0
        else:
            # Bajar por la columna
            for row in range(y, size):
                bit_index = procesar_posicion(matriz, row, x, bitstream, bit_index)
                pasos += 1
                if pasos >= max_pasos or bit_index >= len(bitstream):
                    break
                # También procesamos la columna de la izquierda si existe
                if x - 1 >= 0:
                    bit_index = procesar_posicion(matriz, row, x - 1, bitstream, bit_index)
                    pasos += 1
                    if pasos >= max_pasos or bit_index >= len(bitstream):
                        break
            y = size - 1  # Después de bajar, estamos en la última fila
        
        # Cambiar dirección y moverse a la siguiente columna par
        direction_up = not direction_up
        x -= 2  # Saltamos de columna par a par (o impar a impar)
        
        # Verificación de seguridad
        if pasos >= max_pasos:
            break
    
    return matriz


def procesar_posicion(matriz, row, col, bitstream, bit_index):
    """
    Procesa una posición individual en la matriz con datos del bitstream.
    Retorna el nuevo índice en el bitstream.
    """
    if bit_index >= len(bitstream):
        return bit_index
        
    if matriz[row][col] is None:
        # Usar el bit actual del bitstream
        bit_value = int(bitstream[bit_index])
        matriz[row][col] = bit_value
        return bit_index + 1
    else:
        # Posición ocupada, no avanzar en el bitstream
        return bit_index
