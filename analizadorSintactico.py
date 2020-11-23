import ply.yacc as yacc
from analizadorLexico import tokens

#MIGUEL
def p_sentencias_estructuras(p):
  '''sentencias_estructuras : asignacion
                            | llamada_a_funciones
                            | impresiones
                            | estructuras_de_control
                            | incrementos_decrementos_concatenacion
                            | comentarios  
                            | sentencias_estructuras sentencias_estructuras
'''

def p_creacion_funciones(p):
  '''creacion_funciones : FUNCTION NOMBRE_FUNCION PARENTESIS_I argumentos_funciones PARENTESIS_D LLAVE_I sentencias_estructuras retornar_valores LLAVE_D
  '''
def p_argumentos_funciones(p):
  '''argumentos_funciones : VARIABLE COMA argumentos_funciones
                          | VARIABLE
                          | empty
  '''
def p_retornar_valores(p):
  '''retornar_valores : RETURN valor_i_c PUNTO_COMA
                      | RETURN funciones_creadas 
                      | empty
  '''
#Odalys
def p_comentarios(p):
  '''comentarios : COMMENT
  '''
def p_empty(p):
  '''empty :
  '''
#MIGUEL
def p_llamda_a_funciones(p):
  '''llamada_a_funciones  : metodos PARENTESIS_I VARIABLE PARENTESIS_D PUNTO_COMA
                          | funcion_str_repeat
                          | funciones_creadas
  '''
def p_metodos(p):
  '''metodos  : STR_SHUFFLE
              | SHUFFLE
              | ARRAY_KEY_FIRST
  '''
def p_funciones_creadas(p):
  '''funciones_creadas : NOMBRE_FUNCION PARENTESIS_I operacion_matematica PARENTESIS_D PUNTO_COMA
  '''
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


#Miguel
def p_operadores_comp(p):
  '''operadores_comp  : IGUALDAD
                      | DESIGUALDAD
                      | MAYOR_QUE
                      | MENOR_QUE
                      | MENOR_IGUAL
                      | MAYOR_IGUAL
  '''
def p_operadores_matematicos(p):
  '''operadores_matematicos : MAS
                            | MENOS
                            | POR
                            | DIVIDE
                            | MODULO
  '''
def p_operadores_logicos(p):
  '''operadores_logicos : AND
                        | OR
  '''

#MIGUEL
def p_valor_comp(p):
  '''valor_comp : NUMERO
                | VARIABLE
                | booleans
  '''
def p_valor_negacion(p):
  '''valor_negacion : VARIABLE
                    | booleans
  '''
def p_booleans(p):
  '''booleans : TRUE
              | FALSE
  '''
def p_valor_impresion(p):
  '''valor_impresion  : STRING
                      | VARIABLE
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