# Generated from grammarcode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammarcodeParser import grammarcodeParser
else:
    from grammarcodeParser import grammarcodeParser

# This class defines a complete listener for a parse tree produced by grammarcodeParser.
class grammarcodeListener(ParseTreeListener):

    # Enter a parse tree produced by grammarcodeParser#program.
    def enterProgram(self, ctx:grammarcodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#program.
    def exitProgram(self, ctx:grammarcodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#inicioBloque.
    def enterInicioBloque(self, ctx:grammarcodeParser.InicioBloqueContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#inicioBloque.
    def exitInicioBloque(self, ctx:grammarcodeParser.InicioBloqueContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#statement.
    def enterStatement(self, ctx:grammarcodeParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#statement.
    def exitStatement(self, ctx:grammarcodeParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#asignacion.
    def enterAsignacion(self, ctx:grammarcodeParser.AsignacionContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#asignacion.
    def exitAsignacion(self, ctx:grammarcodeParser.AsignacionContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#tipo.
    def enterTipo(self, ctx:grammarcodeParser.TipoContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#tipo.
    def exitTipo(self, ctx:grammarcodeParser.TipoContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#expression.
    def enterExpression(self, ctx:grammarcodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#expression.
    def exitExpression(self, ctx:grammarcodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#valor.
    def enterValor(self, ctx:grammarcodeParser.ValorContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#valor.
    def exitValor(self, ctx:grammarcodeParser.ValorContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#ciclo.
    def enterCiclo(self, ctx:grammarcodeParser.CicloContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#ciclo.
    def exitCiclo(self, ctx:grammarcodeParser.CicloContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#repetirCiclo.
    def enterRepetirCiclo(self, ctx:grammarcodeParser.RepetirCicloContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#repetirCiclo.
    def exitRepetirCiclo(self, ctx:grammarcodeParser.RepetirCicloContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#mientrasCiclo.
    def enterMientrasCiclo(self, ctx:grammarcodeParser.MientrasCicloContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#mientrasCiclo.
    def exitMientrasCiclo(self, ctx:grammarcodeParser.MientrasCicloContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#condicional.
    def enterCondicional(self, ctx:grammarcodeParser.CondicionalContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#condicional.
    def exitCondicional(self, ctx:grammarcodeParser.CondicionalContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#condition.
    def enterCondition(self, ctx:grammarcodeParser.ConditionContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#condition.
    def exitCondition(self, ctx:grammarcodeParser.ConditionContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#definicionFuncion.
    def enterDefinicionFuncion(self, ctx:grammarcodeParser.DefinicionFuncionContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#definicionFuncion.
    def exitDefinicionFuncion(self, ctx:grammarcodeParser.DefinicionFuncionContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#parameters.
    def enterParameters(self, ctx:grammarcodeParser.ParametersContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#parameters.
    def exitParameters(self, ctx:grammarcodeParser.ParametersContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:grammarcodeParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:grammarcodeParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#arguments.
    def enterArguments(self, ctx:grammarcodeParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#arguments.
    def exitArguments(self, ctx:grammarcodeParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by grammarcodeParser#printStatement.
    def enterPrintStatement(self, ctx:grammarcodeParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by grammarcodeParser#printStatement.
    def exitPrintStatement(self, ctx:grammarcodeParser.PrintStatementContext):
        pass



del grammarcodeParser