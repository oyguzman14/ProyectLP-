import ply.yacc as yacc
from analizadorLexico import tokens

#Arlette
def p_sentencias(p):
  '''sentencias : INICIO sentencias FIN
                | asignacion
                | llamada_a_funciones
                | impresiones
                | estructuras_de_control
                | incrementos_decrementos_concatenacion
                | creacion_funciones
                | asigancion_funciones
                | comentarios
                | sentencias sentencias
  '''

#MIGUEL
def p_sentencias_estructuras(p):
  '''sentencias_estructuras : asignacion
                            | llamada_a_funciones
                            | impresiones
                            | estructuras_de_control
                            | incrementos_decrementos_concatenacion
                            | comentarios
                            | asigancion_funciones
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
#Odalys
def p_incrementos_decrementos_concatenacion(p):
  '''incrementos_decrementos_concatenacion : incremento_decremento PUNTO_COMA
                                           | incrementoc_decrementoc PUNTO_COMA
                                           | concatenacion  PUNTO_COMA
  '''
def p_incremento_decremento(p):
  '''incremento_decremento  : INCREMENTO VARIABLE
                            | DECREMENTO VARIABLE
                            | VARIABLE INCREMENTO
                            | VARIABLE DECREMENTO
  '''
def p_incrementoc_decrementoc(p):
  '''incrementoc_decrementoc : VARIABLE INCREMENTO_C valor_i_c
                            | VARIABLE DECREMENTO_C valor_i_c
  '''
def p_concatenacion(p):
  '''concatenacion : VARIABLE CONCATENA_C STRING
  '''

#Arlette

def p_estructuras_de_control(p):
  '''estructuras_de_control : sentencia_if
                            | sentencia_while
                            | sentencia_foreach
  '''
def p_sentencia_foreach(p):
  '''sentencia_foreach : FOREACH PARENTESIS_I VARIABLE AS VARIABLE PARENTESIS_D LLAVE_I sentencias_estructuras LLAVE_D
  '''

#MIGUEL
def p_sentencia_while(p):
  '''sentencia_while : WHILE PARENTESIS_I argumentos_estructuras PARENTESIS_D LLAVE_I sentencias_estructuras LLAVE_D
  '''
#Odalys
def p_sentencia_if(p):
  '''sentencia_if : IF PARENTESIS_I argumentos_estructuras PARENTESIS_D LLAVE_I sentencias_estructuras LLAVE_D estructura_else
  '''
def p_estructura_else(p):
  '''estructura_else  : ELSE LLAVE_I sentencias_estructuras LLAVE_D
                      | empty
  '''
def p_aregumentos_estructuras(p):
  '''argumentos_estructuras : operacion_logica
                            | operacion_comparacion
  '''

def p_asigancion_funciones(p):
  ''' asigancion_funciones : VARIABLE IGUAL llamada_a_funciones
  '''

#Miguel
def p_llamda_a_funciones(p):
  '''llamada_a_funciones  : metodos PARENTESIS_I VARIABLE PARENTESIS_D PUNTO_COMA
                          | funcion_str_repeat
                          | funciones_creadas
                          | array_key_first
  '''
def p_metodos(p):
  '''metodos  : STR_SHUFFLE
              | SHUFFLE
  '''
def p_funciones_creadas(p):
  '''funciones_creadas : NOMBRE_FUNCION PARENTESIS_I operacion_matematica PARENTESIS_D PUNTO_COMA
  '''

#Arlette
def p_funcion_str_repeat(p):
  ''' funcion_str_repeat : STR_REPEAT PARENTESIS_I STRING COMA NUMERO PARENTESIS_D PUNTO_COMA
  '''
def p_array_key_first(p):
  '''array_key_first : ARRAY_KEY_FIRST PARENTESIS_I VARIABLE PARENTESIS_D PUNTO_COMA
  '''

#Odalys Guzman
def p_impresiones(p):
  '''impresiones  : ECHO argumentos_impresion PUNTO_COMA
                  | PRINT valor_impresion PUNTO_COMA
  '''
def p_argumentos_impresion(p):
  '''argumentos_impresion : valor_impresion COMA argumentos_impresion
                          | valor_impresion
  '''

#Arlette
def p_asignacion(p):
  '''asignacion : VARIABLE IGUAL cuerpo_asignacion PUNTO_COMA
  '''
def p_cuerpo_asignacion(p):
  '''cuerpo_asignacion  : expresion
                        | operacion_logica
                        | STRING
                        | booleans
                        | crear_array
  '''

#Odalys
def p_crear_array(p):
  '''crear_array : ARRAY PARENTESIS_I estructura_array PARENTESIS_D
  '''
def p_estructura_array(p):
  '''estructura_array : estructura_array_c_v
                      | estructura_array_v
  '''

#Arlette
def p_estructura_array_c_v(p):
  '''estructura_array_c_v : valor_array FLECHA valor_array COMA estructura_array
                          | valor_array FLECHA valor_array
  '''
def p_estructura_array_v(p):
  '''estructura_array_v : valor_array COMA estructura_array_v
                        | valor_array
  '''

def p_expresion(p):
  '''expresion  : operacion_comparacion
                | operacion_matematica
  '''

def p_operacion_logica(p):
  '''operacion_logica : operacion_comparacion operadores_logicos operacion_comparacion
                      | valor_negacion operadores_logicos valor_negacion
                      | NEGACION valor_negacion
  '''
def p_operacion_comparacion(p):
  '''operacion_comparacion  : valor_comp operadores_comp valor_comp
                            | PARENTESIS_I valor_comp operadores_comp valor_comp PARENTESIS_D
  '''
def p_operacion_matematica(p):
  '''operacion_matematica : operacion_matematica operadores_matematicos operacion_matematica
                          | PARENTESIS_I operacion_matematica PARENTESIS_D
                          | operacionU operacion_matematica
                          | valor
  '''
def p_operacionU(p):
  '''operacionU : MENOS
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

#Arlette
def p_error(p):
  print("Error de sintaxis")

parser = yacc.yacc()

try:
  p=open('codigo2.txt', 'r')
  s=''
  for linea in p:
    s+=linea.replace('\n' ,' '). replace( '\t',' ')
except EOFError:
  print('Error')

if not s: print('No error')

result=parser.parse(s)
print(result)