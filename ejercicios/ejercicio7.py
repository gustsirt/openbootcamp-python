import ejercicio7modulo as ope

a = 10
b = 2

print( "{} {} {} = {}".format(a,"+",b,ope.suma(a,b)))
print( "{} {} {} = {}".format(a,"-",b,ope.restar(a,b)))
print( "{} {} {} = {}".format(a,"*",b,ope.multiplicar(a,b)))
print( "{} {} {} = {}".format(a,"/",0,ope.dividir(a,0)))
print( "{} {} {} = {}".format(a,"/",b,ope.dividir(a,b)))