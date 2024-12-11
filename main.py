import os
from antlr4 import *
from grammarcodeLexer import grammarcodeLexer
from grammarcodeParser import grammarcodeParser
from Traductor2 import Traductor2

def main():
    # Leer el nombre del archivo de entrada y salida
    in_file = input('Nombre del archivo de entrada (lenguaje inventado) > ')
    out_file = input('Nombre del archivo de salida (Python) > ')

    # Obtener la ruta de la carpeta actual
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Rutas completas de los archivos
    in_code_path = os.path.join(current_dir, in_file)
    out_code_path = os.path.join(current_dir, out_file)

    try:
        # Leer el archivo de entrada
        with open(in_code_path, 'r') as file:
            input_stream = InputStream(file.read())

        # Analizar el código con ANTLR
        lexer = grammarcodeLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = grammarcodeParser(token_stream)
        tree = parser.program()  # Regla raíz

        # Traducir el árbol de análisis a Python usando el listener
        traduccion_listener = Traductor2()
        walker = ParseTreeWalker()
        walker.walk(traduccion_listener, tree)

        # Obtener el código Python traducido
        codigo_python = traduccion_listener.get_code()

        # Guardar el código Python en el archivo de salida
        with open(out_code_path, 'w') as file:
            file.write(codigo_python)

        print(f"Traducción completada. Código Python guardado en: {out_file}")

    except Exception as e:
        print(f"Error durante la traducción: {str(e)}")

if __name__ == '__main__':
    main()
