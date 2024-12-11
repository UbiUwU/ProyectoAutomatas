grammar grammarcode;

// Reglas léxicas
INICIO: 'Inicio';
TERMINAR: 'Terminar';
ESCRIBE: 'Escribe';
LEE: 'Lee';
SI: 'SI';
SINO: 'SINO';
HACER: 'Hacer';
FIN: 'Fin';
REPETIR: 'Repetir';
VECES: 'veces';
MIENTRAS: 'Mientras';
ENTERO: 'entero';
DECIMAL: 'decimal';
PALABRA: 'palabra';
ESVERDAD: 'esVerdad';
REGRESAR: 'regresar';
RECIPE: 'receta';
MAS: 'mas';
MENOS: 'menos';
POR: 'por';
ENTRE: 'entre';
POTENCIA: 'potencia';
RAIZ: 'raiz';
IDENTIFIER: [a-zA-Z][a-zA-Z0-9]*;
DECIMAL_NUMBER: [0-9]+ '.' [0-9]+; // Números con punto decimal
NUMBER: [0-9]+; // Números enteros
STRING: '"' (~["\\] | '\\' .)* '"'; // Cadena entre comillas
BOOLEAN_TRUE: 'si'; // Valores booleanos "verdadero" o "si"
BOOLEAN_FALSE: 'no'; // Valores booleanos "falso" o "no"
WS: [ \t\r\n]+ -> skip; // Ignorar espacios en blanco
LPAREN: '(';
RPAREN: ')';
ARROW: '->';
COMMA: ',';
LESS: '<';
GREATER: '>';
LEQ: '<=';
GEQ: '>=';
EQ: '==';
NEQ: '!=';
LBRACKET: '[';
RBRACKET: ']';

// Reglas sintácticas
program: (inicioBloque | statement)* TERMINAR;

inicioBloque: INICIO LPAREN RPAREN statement+;

statement: asignacion
         | ciclo
         | condicional
         | definicionFuncion
         | llamadaFuncion
         | printStatement;

asignacion: tipo IDENTIFIER ARROW expression;

tipo: ENTERO | DECIMAL | PALABRA | 'esVerdad';

expression: expression MAS expression
          | expression MENOS expression
          | expression POR expression
          | expression ENTRE expression
          | expression POTENCIA expression
          | RAIZ expression
          | IDENTIFIER
          | valor;

valor: DECIMAL_NUMBER
     | NUMBER
     | STRING
     | BOOLEAN_TRUE
     | BOOLEAN_FALSE;

ciclo: repetirCiclo | mientrasCiclo;

repetirCiclo: REPETIR NUMBER VECES HACER statement+ FIN;

mientrasCiclo: MIENTRAS LPAREN condition RPAREN HACER statement+ FIN;

condicional: SI LPAREN condition RPAREN HACER statement+ (SINO HACER statement+)? FIN;

condition: expression (LESS | GREATER | LEQ | GEQ | EQ | NEQ) expression;

definicionFuncion: RECIPE IDENTIFIER LPAREN parameters? RPAREN HACER statement+ (REGRESAR expression)? FIN;

parameters: tipo IDENTIFIER (COMMA tipo IDENTIFIER)*;

llamadaFuncion: IDENTIFIER LPAREN arguments? RPAREN;

arguments: expression (COMMA expression)*;

printStatement: ESCRIBE LPAREN expression RPAREN;
