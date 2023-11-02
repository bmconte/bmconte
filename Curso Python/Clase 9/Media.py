def calcular_media_desde_input():
    numeros = []
    while True:
        entrada = input("Ingresa un número (o 'fin' para calcular la media): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada no válida. Ingresa un número válido o 'fin' para calcular la media.")

    if not numeros:
        return 0  # Devolver 0 si no se ingresaron números
    suma = sum(numeros)
    media = suma / len(numeros)
    return media

# Ejemplo de uso:
media = calcular_media_desde_input()
print("La media es:", media)

