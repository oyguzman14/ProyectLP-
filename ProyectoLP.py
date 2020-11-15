import ply.lex as lex

reservadas={
        #Miguel
        "while":"WHILE",
        "echo": "ECHO",
        "print": "PRINT",
        "shuffle":"SHUFFLE",
        "function":"FUNCTION",
	}

tokens=(#MIGUEL
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
        )+tuple(reservadas.values())

#MIGUEL
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


#MIGUEL
def t_NOMBRE_FUNCION(t):
        r'[a-zA-Z][a-zA-Z0-9_]*'
        if t.value in list(reservadas.keys()):
                t.type=t.value.upper()
        return t


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'


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


