print('Caclculo de indice de masa corporal')
peso = int(input("ingresa su peso: "))
altura = float(input("ingresa su altura en metros: "))
imc = round(peso/altura**2,2)


print("Tu índice de masa corporal es:",imc)
