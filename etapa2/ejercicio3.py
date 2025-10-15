#calcular decibeles
#pedir los decibeles y guardarlo en variable entera
print("calcula de decibeles")
TALADRO=130
PODADORA=106
ALARMA=60
CUARTO=40
decibeles=int(input("ingresa un numero de decibeles"))
if  decibeles <=0:
    print("error, el numero de decibeles debe ser positivo")
elif decibeles <= CUARTO:
    print("el ruido es igual o menor al de un cuarto tranquilo")
elif decibeles >CUARTO and decibeles<= ALARMA:
    print("el ruido esta entre un cuarto tranquilo y un alarma de reloj")
elif decibeles >ALARMA and decibeles <= PODADORA:
    print("el ruido esta entre una alarma de reloj y una podadora")
elif decibeles >PODADORA and decibeles <TALADRO:
    print("el ruido esta entre una podadora y un taladro")
else:
    print("el ruido es mayor al de un taladro")