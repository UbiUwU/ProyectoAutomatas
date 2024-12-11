# Generated from grammarcode.g4 by ANTLR 4.13.2
from antlr4 import *
from grammarcodeLexer import grammarcodeLexer
from grammarcodeParser import grammarcodeParser
if "." in __name__:
    from .grammarcodeParser import grammarcodeParser
else:
    from grammarcodeParser import grammarcodeParser

from antlr4 import ParseTreeListener

from antlr4 import *
from grammarcodeParser import grammarcodeParser
from grammarcodeListener import grammarcodeListener


class Traductor2(grammarcodeListener):
    def __init__(self):
        self.code = []  # Lista para almacenar las líneas traducidas
        self.indent_level = 1  # Nivel de indentación inicial para el cuerpo de main()
        self.inside_loop = False  # Variable para saber si estamos dentro de un ciclo
        self.inside_while = False  # Variable para saber si estamos dentro de un ciclo while

    def enterProgram(self, ctx: grammarcodeParser.ProgramContext):
        self.code.append("def main():")  # Inicio de la función main

    def exitProgram(self, ctx: grammarcodeParser.ProgramContext):
        self.code.append("if __name__ == '__main__':")
        self.code.append("    main()")  # Final del programa

    def enterRepetirCiclo(self, ctx: grammarcodeParser.RepetirCicloContext):
        # Traducir el inicio del ciclo
        repeticiones = ctx.NUMBER().getText()
        self.code.append(f"{self.get_indent()}for _ in range({repeticiones}):")
        
        # Incrementar nivel de indentación para las instrucciones dentro del ciclo
        self.indent_level += 1
        self.inside_loop = True  # Estamos dentro de un ciclo

    def exitRepetirCiclo(self, ctx: grammarcodeParser.RepetirCicloContext):
        # Reducir nivel de indentación después de cerrar el ciclo
        self.indent_level -= 1
        self.inside_loop = False  # Salimos del ciclo

    def enterMientrasCiclo(self, ctx: grammarcodeParser.MientrasCicloContext):
        # Traducir el inicio del ciclo while
        condicion = self.translate_expression(ctx.condition())  # Cambiar 'condicion' por 'condition'
        self.code.append(f"{self.get_indent()}while ({condicion}):")
        
        # Incrementar nivel de indentación para las instrucciones dentro del ciclo
        self.indent_level += 1
        self.inside_while = True  # Estamos dentro de un ciclo while
        

    def exitMientrasCiclo(self, ctx: grammarcodeParser.MientrasCicloContext):
        # Reducir nivel de indentación después de cerrar el ciclo while
        self.indent_level -= 1
        self.inside_while = False  # Salimos del ciclo while

    def enterAsignacion(self, ctx: grammarcodeParser.AsignacionContext):
        # Obtener tipo, nombre de variable y valor
        tipo = ctx.getChild(0).getText()
        var_name = ctx.getChild(1).getText()
        valor_ctx = ctx.getChild(3)
        valor = self.translate_expression(valor_ctx)

        # Traducir tipo si es necesario
        if tipo == "esVerdad":
            if valor.lower() in ["si", "verdadero"]:
                valor = "True"
            elif valor.lower() in ["no", "falso"]:
                valor = "False"
        elif tipo == "palabra":
            valor = f'{valor}'

        # Agregar la línea traducida
        self.code.append(f"{self.get_indent()}{var_name} = {valor}")

    def enterPrintStatement(self, ctx: grammarcodeParser.PrintStatementContext):
        mensaje = ctx.getChild(2).getText()  # Extrae el contenido del `Escribe`
        
        # Si estamos dentro de un ciclo, agregar la indentación correcta
        if self.inside_loop or self.inside_while:
            self.code.append(f"{self.get_indent()}print({mensaje})")  # Traducir a `print`
        else:
            self.code.append(f"    print({mensaje})")  # Traducir a `print`

    def get_indent(self):
        """Genera el nivel de indentación actual basado en self.indent_level."""
        return "    " * self.indent_level

    def translate_expression(self, ctx):
        # Traducir expresiones matemáticas y valores simples
        if ctx.getChildCount() > 1:
            izquierdo = self.translate_expression(ctx.getChild(0))
            operador = ctx.getChild(1).getText()
            derecho = self.translate_expression(ctx.getChild(2))

            operadores = {
                "mas": "+",
                "menos": "-",
                "por": "*",
                "entre": "/",
                "potencia": "**",
                "raiz": "sqrt"  # Si es necesario para tu gramática
            }
            
            comparadores = {
                "menor": "<",
                "mayor": ">",
                "menorIgual": "<=",
                "mayorIgual": ">=",
                "igual": "==",
                "distinto": "!="
            }

            # Verifica si el operador es una comparación
            if operador in comparadores:
                return f"({izquierdo} {comparadores[operador]} {derecho})"

            # Si no es una comparación, traducir la operación matemática
            if operador in operadores:
                return f"({izquierdo} {operadores[operador]} {derecho})"

        # Si solo es un valor simple
        return ctx.getText()


    def get_code(self):
        """Devuelve el código traducido como una cadena."""
        return "\n".join(self.code)
