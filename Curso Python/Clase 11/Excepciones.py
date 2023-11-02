def div():
    try:
        a = int(input("Ingresa el valor de 'a': "))
        b = int(input("Ingresa el valor de 'b': "))
        result = a / b
        return result
    except ValueError:
        return "Error: Debes ingresar valores enteros"
    except ZeroDivisionError:
        return "Error: No es posible dividir por cero"

result = div()
print(f"El resultado de la división es: {result}")
