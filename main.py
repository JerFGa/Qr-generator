import matriz_Base
from URL_binario import encode
##bits = encode()
##print(f"Bits generados:\n{bits}")
##print(f"Cantidad de bits: {len(bits)}")
matriz = matriz_Base.create_qr_matrix()
matriz_Base.patronesDeDeteccion(matriz)
matriz_Base.patronDeAlineacion(matriz)
matriz_Base.lineas_sincronizacion(matriz)
matriz_Base.reservar_modulos_especiales(matriz)
matriz_Base.print_qr_matrix(matriz)
matriz_Base.mostrar_matriz_grafica(matriz)
##print(matriz_Base.print_qr_matrix(matriz_Base.create_qr_matrix()))
