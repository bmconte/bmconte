def suma(numero1, numero2):
    total = numero1 + numero2
    mensaje = f"El Resultado es: {total}"
    return mensaje

num1 = int(input("Ingrese Primer Numero a Sumar: "))
num2 = int(input("Ingrese Segundo Numero a Sumar: "))
print(suma(num1, num2))
