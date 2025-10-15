#constante dias por año que se defina con 365
#variable se tiene que llamar edad/años se tiene que guardae en enteros
"""
Crear un programa que pregunte al usuario su edad en años y
 calcule cuántos días ha vivido aproximadamente, considerando que un año tiene 365 días.
"""
print("programa que pide la edad y calcula los dias vividos")
DIAS_POR_AÑO=365
edad=int(input("ingresa tu edad"))
diasvividos=DIAS_POR_AÑO* edad 
print("dias vividos",diasvividos)