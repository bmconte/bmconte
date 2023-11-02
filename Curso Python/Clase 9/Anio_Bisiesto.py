def anio_bisiesto(anio):
    if type(anio) != int or anio <= 0:
        return "Error: Ingresa un año válido (número positivo)."

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Bucle infinito para verificar años bisiestos
while True:
    entrada = input("Ingresa un año (o 'fin' para salir): ")

    if entrada.lower() == 'fin':
        break

    try:
        anio = int(entrada)
        resultado = anio_bisiesto(anio)
        if resultado is True:
            print(f"{anio} es un año bisiesto.")
        elif resultado is False:
            print(f"{anio} no es un año bisiesto.")
        else:
            print(resultado)
    except ValueError:
        print("Error: Ingresa un año válido (número positivo).")
