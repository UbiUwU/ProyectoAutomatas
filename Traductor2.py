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
        self.code = []
        self.indent_level = 1
        self.inside_loop = False
        self.inside_while = False
        self.inside_if = False

    def enterProgram(self, ctx: grammarcodeParser.ProgramContext):
        self.code.append("def main():")

    def exitProgram(self, ctx: grammarcodeParser.ProgramContext):
        self.code.append("if __name__ == '__main__':")
        self.code.append("    main()")

    def enterRepetirCiclo(self, ctx: grammarcodeParser.RepetirCicloContext):
        repeticiones = ctx.NUMBER().getText()
        self.code.append(f"{self.get_indent()}for _ in range({repeticiones}):")
        self.indent_level += 1
        self.inside_loop = True

    def exitRepetirCiclo(self, ctx: grammarcodeParser.RepetirCicloContext):
        self.indent_level -= 1
        self.inside_loop = False

    def enterMientrasCiclo(self, ctx: grammarcodeParser.MientrasCicloContext):
        condicion = self.translate_expression(ctx.condition())
        self.code.append(f"{self.get_indent()}while ({condicion}):")
        self.indent_level += 1
        self.inside_while = True

    def exitMientrasCiclo(self, ctx: grammarcodeParser.MientrasCicloContext):
        self.indent_level -= 1
        self.inside_while = False

    def enterCondicional(self, ctx: grammarcodeParser.CondicionalContext):
        condicion = self.translate_expression(ctx.condition())
        self.code.append(f"{self.get_indent()}if ({condicion}):")
        self.indent_level += 1
        self.translate_instrucciones(ctx.statement(0))
        self.indent_level -= 1

        if ctx.SINO():
            self.code.append(f"{self.get_indent()}else:")
            self.indent_level += 1
            self.translate_instrucciones(ctx.statement(1))
            self.indent_level -= 1

    def exitCondicional(self, ctx: grammarcodeParser.CondicionalContext):
        self.inside_if = False

    def enterAsignacion(self, ctx: grammarcodeParser.AsignacionContext):
        tipo = ctx.getChild(0).getText()
        var_name = ctx.getChild(1).getText()
        valor_ctx = ctx.getChild(3)
        valor = self.translate_expression(valor_ctx)

        if tipo == "esVerdad":
            if valor.lower() in ["si", "verdadero"]:
                valor = "True"
            elif valor.lower() in ["no", "falso"]:
                valor = "False"
        elif tipo == "palabra":
            valor = f'{valor}'

        self.code.append(f"{self.get_indent()}{var_name} = {valor}")

    def enterPrintStatement(self, ctx: grammarcodeParser.PrintStatementContext):
        mensaje = ctx.getChild(2).getText()
        self.code.append(f"{self.get_indent()}print({mensaje})")

    def get_indent(self):
        return "    " * self.indent_level

    def translate_expression(self, ctx):
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
                "raiz": "sqrt"
            }

            comparadores = {
                "menor": "<",
                "mayor": ">",
                "menorIgual": "<=",
                "mayorIgual": ">=",
                "igual": "==",
                "distinto": "!="
            }

            if operador in comparadores:
                return f"({izquierdo} {comparadores[operador]} {derecho})"

            if operador in operadores:
                return f"({izquierdo} {operadores[operador]} {derecho})"

        return ctx.getText()

    def translate_instrucciones(self, ctx):
        # Verificar si ctx es una lista
        if isinstance(ctx, list):
            for statement in ctx:
                if isinstance(statement, grammarcodeParser.StatementContext):
                    self.code.append(f"{self.get_indent()}{statement.getText()}")
        else:
            # Si no es una lista, tratarlo como un único StatementContext
            if isinstance(ctx, grammarcodeParser.StatementContext):
                self.code.append(f"{self.get_indent()}{ctx.getText()}")

    def get_code(self):
        return "\n".join(self.code)
