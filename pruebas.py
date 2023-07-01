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
print(ej2)