paises = input("Ingrese una lista de paises separados por coma:\n")
paises = list(paises.split(', '))
paises = set(paises)

print(",".join(sorted(paises)))