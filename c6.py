num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el primer valor: "))
if num1 > num2:
    mod=num1%num2
    if mod==0:
        print(f"{num1} es multiplo de {num2}")
    elif mod!=0:
        print(f"{num1} no es multiplo de {num2}")
if num2 >num1:
    mod=num2%num1
    if mod==0:
         print(f"{num2} es multiplo de {num1}")
    elif mod!=0:
        print(f"{num2} no es multiplo de {num1}")
elif num1==num2:
    print("los numeros son iguales por lo tanto son multiplos")