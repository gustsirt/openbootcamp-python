direccion = 'assets/ej8.txt'

def creararchivo(direccion):
  open(direccion, "xt")

def escribir(direccion,texto):
  f = open(direccion, "wt")
  f.write(texto)
  f.close()

mitexto = 'Hola Mundo'
creararchivo(direccion)
escribir(direccion,mitexto)
