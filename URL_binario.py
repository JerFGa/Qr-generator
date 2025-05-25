def encode():
    url = input("Ingresa la URL: ").strip()

    # Indicador de modo: 4 bits para byte mode
    mode_indicator = "0100"

    # Longitud en bytes (ASCII): 8 bits
    length_in_bytes = len(url.encode("utf-8"))  # más robusto ante caracteres fuera del ASCII
    length_bin = format(length_in_bytes, '08b')

    # Codificar caracteres en binario (byte por byte)
    data_bits = ''.join(format(b, '08b') for b in url.encode('utf-8'))

    # Bitstream final
    bitstream = mode_indicator + length_bin + data_bits

    return bitstream
