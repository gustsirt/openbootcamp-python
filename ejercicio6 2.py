class Alumno:
  nombre = None
  nota = None
  
  def __init__(self, Nombre, Nota):
    self.nombre = Nombre
    self.nota = Nota
  
  def imprimir(self):
    print("Nombre:",self.nombre)
    print("Nota:",self.nota)
  
  def resultado(self):
    if self.nota >= 7:
      print("Alumno Aprobado")
    else:
      print("Alumno Reprobado")

flavia = Alumno("Flavia", 6)
gustavo = Alumno("Gustavo", 10)

flavia.imprimir()
flavia.resultado()
print()
gustavo.imprimir()
gustavo.resultado()
