mes=input("ingresa tu mes de nacimiento: ").title()
dia=int(input("ingresa tu dia de nacimiento: "))
#palabra in range(x,y)
"""
Si el mes es Diciembre y el dia está en un rango de 22, 31 o el mes es Enero y el día 
está en un rango de 1, 20
"""
if (mes == "Diciembre" and dia in range(22,32)) or (mes == "Enero" and dia in range(1,21)):
   print("tu signo zodiacal es capricornio")
elif (mes == "Enero" and dia in range(21,32)) or (mes == "Febrero" and dia in range(1,20)):
   print("tu signo zodiacal es acuario")
elif (mes == "Septiembre" and dia in range (23,31)) or (mes == "Octubre" and dia in range (1,23)):
   print("tu signo zodiacal es libra")
elif (mes == "Octubre" and dia in range (1,23)) or (mes=="Noviembre"and dia in range (1,22)):
   print("tu signo zodiacal es escorpio")
elif (mes == "Julio" and dia in range (23,32)) or ( mes == "Agosto" and dia in range (1,23)):
   print("tu signo zodiacal es leo")
elif (mes == "Agosto" and dia in range (23,32)) or (mes == "Septiembre" and dia in range (1,23)):
   print("tu signo zodiacal es virgo")
elif (mes == "Noviembre" and dia in range (22,31)) or (mes == "Diciembre" and dia in range (1,22)):
   print("tu signo zodiacal es sagiario")
elif (mes == "Febrero" and dia <=29) or (mes == "Marzo" and dia >=20):
   print("tu signo zodiacal es piscis")
elif (mes == "Marzo" and dia <=21) or (mes == "Abril" and dia >=19):
   print("tu signo zodiacal es aries")
elif (mes == "Abril" and dia >=19) or (mes == "Mayo" and dia >=20):
   print("tu signo zodiacal es tauro")
elif (mes == "Mayo" and dia <=21) or (mes == "Junio" and dia >=20):
   print(" tu signo zodiacal es geminis")
elif (mes == "Junio" and dia <=21) or (mes == "Julio" and dia <=22):
   print("tu signo zodiacala es cancer")