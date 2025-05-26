import matriz_Base
import llenado
from URL_binario import encode
from redundancia import generar_correciones

bits = encode()
matrix = matriz_Base.generar_matrix()
bits = generar_correciones(bits,matrix)
matrix = llenado.zigzag(matrix, bits)
matriz_Base.print_qr_matrix(matrix)
matriz_Base.mostrar_matriz_grafica(matrix)
