import ply.yacc as yacc
from analizadorLexico import tokens


#Odalys
def p_impresiones(p):
  '''impresiones  : ECHO argumentos_impresion PUNTO_COMA
                  | PRINT valor_impresion PUNTO_COMA
  '''
def p_argumentos_impresion(p):
  '''argumentos_impresion : valor_impresion COMA argumentos_impresion
                          | valor_impresion
  '''



#Odalys
def p_crear_array(p):
  '''crear_array : ARRAY PARENTESIS_I estructura_array PARENTESIS_D
  '''
def p_estructura_array(p):
  '''estructura_array : estructura_array_c_v
                      | estructura_array_v
  '''



#Odalys Guzman
def p_valor_i_c(p):
  '''valor_i_c  : NUMERO
                | VARIABLE
  '''

#Odalys Guzman
def p_valor_array(p):
  '''valor_array  : NUMERO
                  | STRING
  '''

#Odalys Guzman
def p_valor(p):
  '''valor  : NUMERO
            | VARIABLE
            | DECIMAL
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