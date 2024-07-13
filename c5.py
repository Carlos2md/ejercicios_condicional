current_year=int(input("Por favor ingrese el año actual: "))
year=int(input("Por favor ingrese un año para comparar: "))
if year<current_year:
    print ("Han transcurrido: ", current_year-year, "años")
elif current_year<year:
    print("Faltan", year-current_year,"años")
elif current_year==year:
    print("Los años son iguales")