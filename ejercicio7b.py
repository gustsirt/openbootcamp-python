import time as t

tiempoactual = t.localtime()
hora = t.strftime("%H", tiempoactual)
minutos = t.strftime("%M", tiempoactual)
print (hora, minutos)

if int(hora) > 18:
  print("Es hora de irse a casa")
else:
  print("Faltan {} horas y {} minutos para poder irte a casa".format(17-int(hora), 59-int(minutos)+1))
