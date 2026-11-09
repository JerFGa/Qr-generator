# QR Code Generator from Scratch (Python)

Implementación algorítmica desde cero para la generación de códigos QR (Quick Response) en Python, sin depender de librerías externas generadoras de QR.

## 🚀 Características
- **Codificación Binaria de Datos (`URL_binario.py`):** Conversión de texto y URLs a secuencias de bits según el estándar de codificación QR.
- **Construcción de la Matriz Base (`matriz_Base.py`):** Generación de patrones de búsqueda (Finder Patterns), patrones de alineación, temporización y separadores.
- **Corrección de Errores Reed-Solomon (`redundancia.py`):** Implementación matemática de polinomios generadores y cálculo de bloques de corrección de errores (ECC).
- **Llenado y Enmascaramiento (`llenado.py`):** Algoritmo de recorrido en zigzag de la matriz para colocación de bits de datos y aplicación de máscaras de contraste óptimo.

## 🛠️ Tecnologías y Conceptos
- **Lenguaje:** Python 3
- **Conceptos:** Estructuras de datos matriciales, Aritmética de campos de Galois (Galois Fields GF), polinomios de código cíclico y manipulación a nivel de bits.

## 💻 Uso
```bash
python main.py
```
