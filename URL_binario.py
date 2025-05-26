def encode():
    url = input("Ingresa la URL: ").strip()

    # Paso 1: Indicador de modo (byte mode)
    mode_indicator = "0100"

    # Paso 2: Longitud (en bytes)
    length_in_bytes = len(url.encode("utf-8"))
    length_bits = format(length_in_bytes, '08b')

    # Paso 3: Datos en binario
    data_bits = ''.join(format(b, '08b') for b in url.encode('utf-8'))

    # Paso 4: Construcción inicial
    bitstream = mode_indicator + length_bits + data_bits

    # Paso 5: Terminador de hasta 4 ceros
    max_data_bits = 44 * 8  # versión 2 nivel L: 44 bytes = 352 bits
    terminador = min(4, max_data_bits - len(bitstream))
    bitstream += '0' * terminador

    return bitstream
