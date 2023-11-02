copa_mundial = {
    1990: "Alemania", 1994: "Brasil", 1998: "Francia", 2002: "Brasil", 2006: "Italia", 2010: "España",
    2014: "Alemania", 2018: "Francia", 2022: "Messi Papaaaaa"}

while True:
    fecha = int(input("Ingresa el año a consultar (o introduce '0' para salir): "))

    if fecha == 0:
        break

    if fecha in copa_mundial:
        print(copa_mundial[fecha])
    else:
        print("Ese año no está registrado, ingrese otra fecha.")
