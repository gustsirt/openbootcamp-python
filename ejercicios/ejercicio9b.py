from functools import reduce

def reduccion (lista):
  lista = filter(lambda x: x % 2 != 0, lista)
  lista = reduce( (lambda a, b: a + b), lista)
  return lista


n = int(input("Ingrese un numero para definir el rango de la suma:\n"))
lista = list( range(n))



print (f'La suma de los numeros impares en: {n} arroja el resultado de: {reduccion(lista)}')

