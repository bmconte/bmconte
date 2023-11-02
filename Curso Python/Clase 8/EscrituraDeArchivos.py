#1. Abrir el Archivo
#    a. Ruta donde se encuentra el archivo
#    b. Que Permisos voy a Brindar al Archivo, a> Adicion al archivo, w> Sobreescritura,

#2. Escribir el Archivo
#3. Cerrar el Archivo

# Escritura
f = open("usuario.csv", "a")
f.write("Gay,Loser,Herrera, 37,\n")
f.close()

#Lectura (r > Lectura, rb > Lectura Binaria
# Read: Lectura Completa
# ReadLine: Lectura de una sola linea
# ReadLines: Iterable con la lectura de todas las lineas
with open("usuario.csv") as f:
    f.read()
print(f)

