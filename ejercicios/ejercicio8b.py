import pickle as p

class vehiculo:
  modelo = ''
  color = ''
  puertas = 0
  
  def __init__(self, modelo, color, puertas):
    self.modelo = modelo
    self.color = color
    self.puertas = puertas
  def __str__(self) -> str:
    return self.modelo +' '+ self.color +' '+ str(self.puertas)

fk = vehiculo('Ford K','Negro',3)
print(str(fk))

f = open('ejercicios/assets/ej8vehiculo.bin', 'w+b')
p.dump(fk, f)
f.close()

f2 = open('ejercicios/assets/ej8vehiculo.bin', 'rb')
vehic = p.load(f2)
f2.close()

print(vehic)