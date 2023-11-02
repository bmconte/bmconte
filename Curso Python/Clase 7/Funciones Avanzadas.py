
#Estaba la calavera sentada en su butaca, llegó la muerte y le dijo, comadre por qué está tan flaca.--

txt = input("Ingrese cualquier valor: ")

print(f"El texto en mayúscula es: {txt.upper()}, esto es para Coder")
print(f"El texto en minúscula es: {txt.lower()}, esto es para Coder")
print(f"El texto en Capitalize es: {txt.capitalize()}, esto es para Coder")
print(f"El texto en Title es: {txt.title()}, esto es para Coder")
print(f"La cantidad de caracteres 'a' es: {txt.count('a')}, esto es para Coder")
print(f"Índice del string: {txt.find('')}, esto es para Coder")


print(f"La cadena separada por espacio es: {txt.split()}")
print(f"La cadena separada es: {txt.split('a')}")
print(f"Eliminando los espacios laterales: {txt.strip(' ')}")
print(f"Eliminando los ------- laterales: {txt.strip('-')}")
print(f"Reemplazando valores: {txt.replace('a', 'A')}")