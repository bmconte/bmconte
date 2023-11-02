def es_multiplo(num1, num2):
    if num2 == 0:
        return False

    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

if es_multiplo(num1, num2):
    print(f"{num1} o {num2} es múltiplo del otro.")
else:
    print(f"{num1} y {num2} no son múltiplos el uno del otro.")
