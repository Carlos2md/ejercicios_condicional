area=input("Por favor ingrese (c) para calcular el area de un circulo o (t) para el area de un triangulo: ")
area=area.lower()
if area=="t":
    print("Vamos a calcular el area de un triangulo: ")
    b=int(input("Ingrese la base del triangulo: "))
    a=int(input("Ingrese la altura del triangulo: "))
    areat=((a*b/2))
    print("El area del triangulo es: ",areat)
elif area=="c":
    print("Vamos a calcular el area de un circulo: ")
    r=int(input("Ingrese el radio del circulo: "))
    areac=((3.141516)*(r**2))
    print("El area del circulo es: ", areac)
else:
    print("Opcion invalida")