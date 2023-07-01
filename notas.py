# ********************************************************************************************************************
# ! ******************************************************************************************************************
# TODO Variables - Operadores - y elementos comunes
# --------------------------------------------------------------------------------------------------------------------

# <-- esto es un comentario

# las variables adquieren el tipo segun el contenido que se le ponga al inicio
import collections


numeros = 1
cadenas = 'hola'
booleano = True
flotante = 5.5
lista = [1,2,3]
tuplas = (1,2,3)
print(tuplas[0]) # muestra 1
conjuntos = {1,2,3}
diccionario = {"clave1":0, "clave2":2}
print(diccionario["clave1"]) # muestra 0

# ! operaciones con CADENAS 
# EXTRAER caracter
language = 'Python'
language[0] # es la P - indexación 
language[-1] # es la n - indexación negativa

# EXTRAER rango
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# INVERTIR
greeting = 'Hello, World'
print(greeting[::-1]) # dlroW ,olleH

# SALTEAR CARACTERES (en el ejemplo cada 2 caracteres)
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

# CONCATENAR
#   elementos especiales
string = "\n" # nueva línea
string = "\t" # Tabulador significa (8 espacios)
string = "\\" # barra invertida
string = "\'" # Una frase (')
string = "\"" # : comillas dobles (")

#   ESTILO ANTIGUO
# MODELO = "cadena(con comodines)" %(variables)
# %s - Cadena (o cualquier objeto con una representación de cadena, como números)
# %d - Enteros
# %f - Números de punto flotante
# "%.nf" - Números de punto flotante con precisión fija
string = 'Esto es cadena %s con un entero %d, un flotante %f y un flotando con tamaño fijo %.2f' %(cadenas, numeros, flotante, flotante)
# resultado: Esto es cadena hola con un entero 2, un flotante 5.5 y un flotando con tamaño fijo 5.50

#   ESTILO CASI.ACTUAL -*- (a partir version Python 3)
# MODELO = "cadena(con comodines)".format(variables)
string = 'Esto es cadena {} con un entero {}, un flotante {} y un flotando con tamaño fijo {:.2f}'.format(cadenas, numeros, flotante, flotante)
# resultado: Esto es cadena hola con un entero 2, un flotante 5.5 y un flotando con tamaño fijo 5.50
# opcion 1 : si a cada {0} le pongo un numero {1} .. le indico el orden que va a tomar en la tupla (0, 1, 2, ...)
# opcion 2 : si a cada {num} le pongo un ALIAS {txt} - es alias no te deja poner una variable.. en la tupla hago una especie de diccioanrio (num=numero, txt="hola", ...)

#   ESTILO ACTUAL Fstring
# MODELO = f"cadena(con comodines y variables)"
string = f'Esto es cadena {cadenas} con un entero {numeros}, un flotante {flotante} y un flotando con tamaño fijo {flotante:.2f}'
# resultado: Esto es cadena hola con un entero 2, un flotante 5.5 y un flotando con tamaño fijo 5.50
# a diferencia del metodo anterior, aqui, entre las {} si mencionas variable, lo que implica que ahi dentro tambien pueden poner funciones
string = f'Esto es cadena {cadenas.upper()} con un entero {numeros}, un flotante {flotante} y un flotando con tamaño fijo {flotante:.2f}'

# ********************************************************************************************************************
# ! ******************************************************************************************************************
# TODO Bucles y condicionales (no llevan parentesis, se manejan por la identacion)
# --------------------------------------------------------------------------------------------------------------------

# SI
if False:
  print(numeros)
elif True:        #opcional
  print(cadenas)
else:             #opcional
  pass            #palabr reservada que evita el error de que no se haya declarado nada, ideal para poner un "valor" que debe ser reemplazado

# MIENTRAS (necesita algo que cambie)
contador = 0
while contador < 10:
  contador += 1
  if contador == 4: # opcional se usa para que no se execute lo que esta debajo del continue en esa iteracion
    continue
  if contador == 5:# opcional rompe el bukle
    break

#FOR se us para recorrer lista, tuples => array
lista = (1,2,3,...)
lista = range(5)
for x in lista:  
  print("acciones")
else: # opcional y RARO, se ejecuta siempre que el FOR no tenga un BREAK
  print("acciones")

#IF IN ... se usa como si fuese IF dentro de un FOR
if 4 in lista:  #in o not in
  print("acciones")  # solo se ejecuta si el 4 estuviera en la lista

# FOR PARA DICCIONARIOS -- recorre todos los elementos del diccioanrio
diccionario = {"clave1":0, "clave2":2}
for key, value in diccionario.items():
  print(key,"=",value)

# ! SWITCH solo a partir de la version 3.10 de Python
valor = 1
match valor:
  case 1:
    print("acciones")
  case 2:
    print("acciones")


# ********************************************************************************************************************
# ! ******************************************************************************************************************
# TODO Funciones
# --------------------------------------------------------------------------------------------------------------------

# Las FUNCIONES tienen que estar declaradas ANTES que se las invoque (osea, arriba en el codigo)

# FORMA BASICA
def nombre(parametros): #los parametros son opcionales, peude no estar
  pass
  return parametros #opcional, es el valor que DEVUELVE la funcion - IMPORTANTE, se peude devolver mas de un valor separado por , y sera una tupla

# FORMA ANONIMA (asignada a una variable - usa la palabra reservada LAMBDA)
# se usa para funciones muy simple, de 1 renglon y automaticamente "DEVUELVE" lo que hace
variable = lambda parametros: 1+1 # los parametros son opcionales
print(variable(5))  # ASI SE EJECUTA LA FUNCION -- mostrara 2


# MULTIPLES RETURN
def nombrex(val1=1, val2=2): #los parametros son opcionales, peude no estar
  return val1, val2 

  #hay dos soluciones, en una tupla o en multiple variables
tup = nombrex(1, 3) # tup = (1, 3) -- se asigna como tupla
vall1, vall2 = nombrex(1, 3) # vall1 = 1 y vall2 = 3 -- a cada return se le asigna a una variable

# VARIABLES SHADOWING
valorejemplo = 1
def nombre2():
  valorejemplo = 5 # <--- esta no es la misma variable GLOBAL de arriba, sino una interna

# TOMAR VALOR GLOBAL
def nombre3():
  global valorejemplo 
  valorejemplo = 4 # <--- esta SI es la misma variable GLOBAL de arriba, xq tiene el valor global puesto arriba

# PARAMETRO OPCIONAL
def nombre4(valor0, valor1 = 30): # PARAMETRO OPCIONAL (solo pueden ser los ultimos)
  pass                   # si al momento que invoco la funcion no le doy valor, el valor pasa a ser 30

# NOMBRADO DE PARAMETROS (si se menciona el nombre del parametro puedo, se puede pasar cualqueir paramtero opcional)
def suma (a=1, b=2, c=3):
  print (a+b+collections)
suma(b=5)  # esto indica que solo le pase el valor B como parametro

# PARAMETROS VARIABLES (se toma como lista)
def sumas (*args): #esto indica que se le pueden pasar muchos valores y se interpretaran como una lista
  resultado = 0
  for arg in args:
    resultado += arg
  print(resultado)

sumas(1,2,3,4,5,0,0,6) # es valido
sumas(1,2,3) # es valido

# PARAMETROS DICCIONARIO 
diccionario = {"clave1":0, "clave2":2}
def mostrar (**kwargs): #esto indica que se le pueden pasar muchos valores y se interpretaran como una lista
  print(kwargs["clave1"])

mostrar(diccionario) # muestra 0

# PARAMETROS DICCIONARIO otras opciones 
diccionario = {"clave1":0}
def mostrar (**kwargs):
  clave1 = kwargs['clave1']
  clave2 = kwargs['clave2'] if 'clave2' in kwargs else 0 # VALOR POR DEFECTO esto es similar a poner en JS valor = x || 0


# ! FUNCIONES UTILES

# PPRINT

import pprint
pprint.pprint("elemento") # imprime el contenido en forma diccionario = vertical
dir("elemento") # muestra el contenido de ese elemento

# GLOBALS y LOCALS -- indican que lo el SISTEMA reconoce que existe hasta ese momento (usar con pprint)

globals() # TABLA DE SIMBOLOS --> DEVUELVE DICCIONARIO .. 
ejemplo = 1
globals()['ejemplo'] = 2 # es otra forma de modificar la variable del punto anterior, porque gloabls devuelve un diccionario
# global ejemplo = 2 --- esto es lo mismo que el renglon anterior
locals() # es lo mismo que global pero en LOCAL (en en el ambito entre ( ) -- en python seria lo identado)

# DIR (muestra las funciones o variables de algo)
pprint.pprint(dir(2)) # muestra de un numero
pprint.pprint(dir('')) # muestra de un texto
# ...


# ********************************************************************************************************************
# ! ******************************************************************************************************************
# TODO Clases
# --------------------------------------------------------------------------------------------------------------------

# ! CLASES DINAMICAS (el self es parte de las clases dinamicas)
# primero se declara objeto luego se instancia

# PRIEMRO SE DECLARA OBJETO
class NombreClase:
  variableN = 1
  Variableb = False
  _variable3 = 4         # por BUENA PRACTICA cuando se inicia con _ indica que NO DEBERIA modificar ese dato si no es por funcion (que no tenga _)
  
  def cambiarbooleano (self):
    self.Variableb = not self.Variableb   #el self es una referencia a la clase en si, es obligatoria para hacer referencias a los elementos XQ SINO entiende que estas declarando una variable en vez de usarla
  def _otrafuncion (self):   # por BUENA PRACTICA esta funcion no deberia ser tocada
    pass

# PARA CLASES DINAMICAS: SE LO INSTANCIA
primerlemento = NombreClase()

# ! CLASES ESTATICAS (no incluye el self)
# primero se declara objeto luego se usa el mismo objeto como instancia

class NombreClase:
  variableN = 1
  Variableb = False
  _variable3 = 4  
  
  def cambiarbooleano ():
    NombreClase.Variableb = not NombreClase.Variableb  
  def _otrafuncion ():   
    pass

# ! HERENCIA (una clase que hereda los metodos del padre)
class Abuelo:
  valor = 1

class Padre(Abuelo): #hereda "valor = 1" del padre (abuelo)
  valor2 = 2
  pass

jose = Padre()
jose.valor  #aqui se muestra como se llego a una variable del padre instanciando el hijo

# HERENCIA MULTIPLE (se debe hacer de menor a mayor)
  
class Hijo(Padre, Abuelo): 
  pass

maria = Hijo()
maria.valor2
maria.valor

# ! CONTRUCTOR DE CLASE
class Ejemplo:
  valor0 = 1
  def __init__(self, parametros) -> None:  #asi se define el constructor, que puede o no tener parametros
    self.valor0 = parametros
    
class Ejemplo2 (Ejemplo):
  super.__init__(...)  # invoca constructor de la clase padre

# ! CLASES ABSTRACTAS
# son definiciones "parciales" de una clase padre, que puede obligar a sus hijos realizar ciertas definiciones

# ! COMPOSICION
# instancia otras clases
# es cuando las variables de una clase son otra clase

class Mano:
  dedos = 5

class Brazo:
  mano = Mano()

#ejemplo de uso
b = Brazo
b.mano.dedos

# ! Sobrecarga de funciones - Python permite volver a definir una funcion que viene por sistema
class ejemplo1:
  def __init__(self, num):
    self.num = num
ej1 = ejemplo1(1)
# si hago un print
print(ej1) # obtengo <__main__.ejemplo1 object at 0x00000193CCE4E750>
# QUE ES LO MISMO DECIR
print(str(ej1)) # obtengo <__main__.ejemplo1 object at 0x00000193CCE4E750>

class ejemplo2:
  def __init__(self, num):
    self.num = num
  def __str__(self) -> str:
    return f'El numero es {self.num}'

ej2 = ejemplo2(3)
# si hago un print
print(ej2) # obtengo: "El numero es 3"

#TAMBIEN SE SOBRECARGA __repr__ (que es similar a STR) cuando se quiere mostrar cosas para testeos (no es lo mismo lo que quiero mostrar para el usuario, que para otro programador)


# ********************************************************************************************************************
# ! ******************************************************************************************************************
# TODO Ambito MAIN - y estructura basica
# --------------------------------------------------------------------------------------------------------------------

#. MAIN o en castellano PRINCIPAL, deberia ser la funcion que engloba el programa en si - Y es buena practica
#. todo programa python debe tener:
import pruebas  # van al principio

def main():
  pass # aca va el programa
  pass # aca va el programa
  pass # aca va el programa

# ... y al final de todo
if __name__ == "__main__": # __name__ es la variable que tiene el nombre del archivo, y solo se llama __main__ su es el fichero base
  main()

# ********************************************************************************************************************
# ! ******************************************************************************************************************
# TODO MODULOS -- Import
# --------------------------------------------------------------------------------------------------------------------

#se usa para importar otros archivos .py
# AL IMPORTAR UN MODULO LO QUE "IMPRIME" o EJECUTA SE HACE REALMENTE como si hubiese estado un codigo arriba del otro, lo unico que cambia es la forma de acceder a los elementos (variables, funciones, clases ...)

import ejercicio3 #este es un ejemplo
ejercicio3.altura #asi se llama a una variable, o funcion() de ese archivo (o modulo)

import ejercicio4 as eje4 # asi se hace para llamarlo con otro nombre
eje4.contador #ejemplo con nombre corto

# ! IMPORTAR PAQUETE (o carpeta con ficheros)
# 1 crear carpeta
# 2 dentro de la carpeta crear archivo __init__.py
# 3 importar de alguna de las siguientes formas:
#    a)    import carpeta.fichero --> (se puede incluir as apodo)
#    b)    from carpeta import fichero --> (se puede incluir as apodo)
#    c)    from carpeta import subcarpeta, opc otraSubcarpeta --> (en este caso icnluye todos los archivos.py)
#    d)    from carpeta import * --> (importa todos los que estan en __all__)
#             el archivo __init__.py de la carpeta debe tene una linea con: __all__ = [subcarpeta1, subcarpeta2, ...]
# 4 pasa usarlo: --> paquete.archivo.elemento

# ********************************************************************************************************************
# ! ******************************************************************************************************************
# TODO CONJUNTO DE FUNCIONES DE MANIPULACION DE FICHEROS
# --------------------------------------------------------------------------------------------------------------------

instanciaDeClase = open ('ruta', "permiso")
#ejemplo, usualmento como variable se usa f o file
f = open('notas.txt', 'r') # lo usal es poner rt (read + text)
# permisos
# r = lectura
# a = append (adjuntar al final)
# w = write (borro todo y escribo desde 0)
# x = create
# t = text
# b = binary
# +
# rw = w+ --> lectura escritura
datos = f.read() #adquirir datos - OPCIONAL en read(x) se puede poner la cantidad de bytes que se quiere leer
f.close() #cerrar como buena practica

#f.read(opc: bytes) -- lee todo
#f.readline() -- lee una linea y se ubica en la siguiente (osea que si aplica de nuevo la funcion leere la segunda linea)
#   si texto = "a"
#   se usa con: -*- while texto != "": -*- while len(texto) > 0:
#f.readlines() -- devuelve una lista (txt\n, txt\n, ...)