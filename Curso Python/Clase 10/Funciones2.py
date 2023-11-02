def conversion_longitud(valor):
    if valor < 0:
        return "El valor debe ser un número entero no negativo."
    metros = valor // 1000
    centimetros = (valor % 1000) // 10
    milimetros = (valor % 1000) % 10
    return f"{metros} metros, {centimetros} centímetros, {milimetros} milímetros"

# Ejemplo de uso para convertir a metros, centímetros y milímetros
numero = int(input("Ingrese un número entero en milímetros: "))
resultado = conversion_longitud(numero)
print(resultado)

