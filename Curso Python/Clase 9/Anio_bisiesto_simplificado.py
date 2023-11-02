def anio_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

while True:
    entrada = input("Ingresa un año (o 'fin' para salir): ").lower()

    if entrada == 'fin':
        break

    try:
        anio = int(entrada)
        if anio_bisiesto(anio):
            print(f"{anio} es un año bisiesto.")
        else:
            print(f"{anio} no es un año bisiesto.")
    except ValueError:
        print("Error: Ingresa un año válido (número positivo).")
