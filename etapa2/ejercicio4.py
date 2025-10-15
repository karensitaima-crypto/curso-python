#leer los valores de los triangulos
lado1=int(input("ingresa el valor de un lado:  "))
lado2=int(input("ingresa el valor del segundo lado: "))
lado3=int(input("ingresa el valor del tercer lado del: "))
if (lado1+ lado2> lado3) and (lado1 +lado3> lado2) and (lado2+ lado3> lado1):
   # a == b y b == c
    if lado1 == lado2 and lado2 == lado3:
       print("tu triangulo es equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("tu triangulo es isoseles")
    else:
        print("tu triangulo es escaleno")
else:
    print(" error, esas longitudes no pueden formar un triangulo")

