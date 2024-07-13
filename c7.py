num1= int(input("Por favor ingrese un primer valor: "))
num2= int(input("Por favor ingrese un segundo valor: "))
num3= int(input("Por favor ingrese un tercer valor: "))
if num1==num2 and num2==num3:
    print("Los numeros son iguales")
elif num1==num2 or num2==num3 or num1==num3:
    print("Hay dos(2) numeros iguales")
else :
    print ("Son todos Diferentes")
