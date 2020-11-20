import ply.yacc as yacc
from analizadorLexico import tokens

#EXPRESIONES MATEMATICAS

def p_expresion(p):
  'expresion : valor'

def p_operacionMat(p):
  'expresion : valor operadoresMat expresion'

def p_operadoresMat(p):
  '''operadoresMat  : MAS
                    | MENOS
                    | DIVIDE
                    | POR
                    | MODULO
  '''
def p_valor(p):
  '''valor  : NUMERO
            | VARIABLE
  '''

parser = yacc.yacc()

while True:
  try:
    s=input('>> ')
  except EOFError:
     break
  if not s : continue
  result = parser.parse(s)
  print(result)