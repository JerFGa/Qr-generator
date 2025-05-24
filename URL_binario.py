def encode():
    url = input("Ingresa la URL: ")

    # Modo byte indicador: 4 bits '0100'
    mode_indicator = "0100"

    # Longitud en bytes en 8 bits
    length_bin = format(len(url), '08b')

    # Codificar cada caracter a 8 bits
    data_bits = ''.join(format(ord(c), '08b') for c in url)

    # Construir el bitstream completo
    bitstream = mode_indicator + length_bin + data_bits

    return bitstream

