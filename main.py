import matriz_Base
import llenado
from URL_binario import encode
bits = encode()
#print(f"Bits generados:\n{bits}")
#print(f"Cantidad de bits: {len(bits)}")
matrix = matriz_Base.generar_matrix()
llenado.zigzag_patron_ajedrez(matrix,bits)
matriz_Base.print_qr_matrix(matrix)
matriz_Base.mostrar_matriz_grafica(matrix)
##print(matriz_Base.print_qr_matrix(matriz_Base.create_qr_matrix()))
