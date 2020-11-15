import ply.lex as lex

reservadas={
        #Miguel Rivadeneira
        "while":"WHILE",
        "echo": "ECHO",
        "print": "PRINT",
        "shuffle":"SHUFFLE",
        "function":"FUNCTION",
        #Arlek
        "foreach":"FOREACH",
        "array_key_first":"ARRAY_KEY_FIRST",
	    "as":"AS",
        "array":"ARRAY",
        #Odalys Guzman
        "if":"IF",
        "else":"ELSE",
        "str_repeat":"STR_REPEAT",
        "str_shuffle":"STR_SHUFFLE"
	}

tokens=(
        #Miguel Rivadeneira
        "IGUAL",
        "VARIABLE",
        "MAS",
        "MENOS",
        "POR",
        "DIVIDE",
        "PUNTO_COMA",
        "MODULO",
        "IGUALDAD",
        "DESIGUALDAD",
        "MAYOR_QUE",
        "MENOR_QUE",
        "NOMBRE_FUNCION",
        "STRING",
        #Odalys Guzman
        "AND",
        "OR",
        "NEGACION",
        "PARENTESIS_I",
        "PARENTESIS_D",
        "LLAVE_I",
        "LLAVE_D",
        "NUMERO",
        "DECIMAL",
        "BOOLEAN",
        "COMA",
        #ARLEK
        "FLECHA",
	    "MENOR_IGUAL",
	    "MAYOR_IGUAL",
	    "INCREMENTO",
	    "DECREMENTO",
	    "INCREMENTO_C",
	    "DECREMENTO_C",
	    "CONCATENA_C",
	    "INCIO",
	    "FIN",
        "COMMENT"
        )+tuple(reservadas.values())

#Miguel Rivadeneira
t_IGUAL=r'='
t_VARIABLE=r'(\$([a-z]|[A-Z]))([a-zA-Z0-9]+)?'
t_MAS=r'\+'
t_MENOS=r'\-'
t_POR=r'\*'
t_DIVIDE=r'\/'
t_PUNTO_COMA=r';'
t_MODULO=r'\%'
t_IGUALDAD=r'=='
t_DESIGUALDAD=r'\!\='
t_MAYOR_QUE=r'>'
t_MENOR_QUE=r'<'
t_WHILE=r'while'
t_ECHO=r'echo'
t_PRINT=r'print'
t_SHUFFLE=r'shuffle'
t_STRING=r'(\"[\w\s\\n]+\"|\'[\w\s\\n]+\')'
t_FUNCTION=r'function'

#ARLEK
t_MENOR_IGUAL=r'\<='
t_MAYOR_IGUAL=r'\>='
t_INCREMENTO=r'\+\+'
t_DECREMENTO=r'\-\-'
t_INCREMENTO_C=r'\+='
t_DECREMENTO_C=r'\-='
t_CONCATENA_C=r'\.='
t_INCIO=r'<\?php'
t_FIN=r'\?.'
t_FLECHA=r'=>'
t_FOREACH=r'foreach'
t_ARRAY_KEY_FIRST=r'array_key_first'
t_AS=r'as'
t_ARRAY=r'array'


#Odalys Guzman
t_AND=r'and'
t_OR=r'or'
t_NEGACION=r'\!'
t_PARENTESIS_I=r'\('
t_PARENTESIS_D=r'\)'
t_LLAVE_I=r'\{'
t_LLAVE_D=r"\}"
t_NUMERO=r'\d+'
t_DECIMAL=r'[+-]?[0-9]*\.[0-9]+'
t_BOOLEAN=r'(true|false|[0-1])'
t_COMA=r'\,'
t_IF=r'if'
t_STR_REPEAT=r'str_repeat'
t_STR_SHUFFLE=r'str_shuffle'
t_ELSE=r'else'


#Miguel Rivadeneira
def t_NOMBRE_FUNCION(t):
        r'[a-zA-Z][a-zA-Z0-9_]*'
        if t.value in list(reservadas.keys()):
                t.type=t.value.upper()
        return t


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

#Odalys Guzman
def t_COMMENT(t):
        r'\#.*'
        pass

#Arlek
def t_error(t):
	print("No es reconocido '%s'" % t.value[0])
	t.lexer.skip(1)


lexer=lex.lex()
data=open("codigo.txt",'r')

for i in data:
	print(">> "+i)
	lex.input(i)
	while True:
		tok = lexer.token()
		if not tok:
			break  # No more input
		print(tok)


