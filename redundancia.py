from reedsolo import RSCodec

def generar_correciones(bitstream_binario, matriz):
    """
    Aplica Reed–Solomon ECC para QR versión 2, nivel M (media corrección).
    Devuelve un bitstream binario con datos + bits de corrección,
    y lo rellena con ceros hasta llenar todos los espacios nulos.
    """
    datos_bytes = 28
    ecc_bytes = 6

    # Convertir binario a bytes
    datos = [int(bitstream_binario[i:i+8], 2) for i in range(0, len(bitstream_binario), 8)]

    if len(datos) > datos_bytes:
        raise ValueError(f"❌ El mensaje excede los {datos_bytes} bytes permitidos en nivel M (usa {len(datos)}).")

    # Rellenar los datos con ceros hasta 28 bytes
    datos += [0] * (datos_bytes - len(datos))

    # Aplicar Reed-Solomon
    rs = RSCodec(ecc_bytes)
    codificado = rs.encode(bytes(datos))  # devuelve datos + corrección

    bitstream_corregido = ''.join(format(b, '08b') for b in codificado)

    # Contar posiciones None en la matriz
    bits_vacios = sum(1 for fila in matriz for celda in fila if celda is None)

    # Rellenar con ceros si quedan espacios vacíos
    if len(bitstream_corregido) < bits_vacios:
        bitstream_corregido += '0' * (bits_vacios - len(bitstream_corregido))

    return bitstream_corregido
