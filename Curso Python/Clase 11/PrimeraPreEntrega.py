# Diccionario para almacenar usuarios y contraseñas
usuarios = {}
# Diccionario para almacenar el usuario y la contraseña del administrador
administrador = {"usuario": "admin", "contrasena": "Admin"}  # Usuario y contraseña del administrador

# Función para registrar un nuevo usuario
def registrar_usuario(usuario, contrasena):
    if usuario == administrador["usuario"]:
        print("El nombre de usuario 'admin' no puede ser creado por nuevos usuarios.")
    elif usuario not in usuarios:
        usuarios[usuario] = contrasena
        print("Usuario registrado exitosamente.")
    else:
        print("El usuario ya existe. Por favor, elige otro nombre de usuario.")

# Función para mostrar la información de los usuarios almacenados
def mostrar_usuarios():
    contrasena_admin = input("Introduce la contraseña de administrador: ")
    if contrasena_admin == administrador["contrasena"]:
        print("Usuarios registrados:")
        for usuario, contrasena in usuarios.items():
            print(f"Usuario: {usuario}, Contraseña: {contrasena}")
    else:
        print("Credenciales de administrador incorrectas. Acceso denegado.")

# Función para iniciar sesión
def iniciar_sesion(usuario, contrasena):
    if usuario in usuarios and usuarios[usuario] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Credenciales incorrectas. Por favor, intenta de nuevo.")

# Función principal del programa
def main():
    while True:
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados (Requiere contraseña de administrador)")
        print("3. Iniciar sesión")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            usuario = input("Introduce tu nombre de usuario: ")
            contrasena = input("Introduce tu contraseña: ")
            registrar_usuario(usuario, contrasena)
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            usuario = input("Introduce tu nombre de usuario: ")
            contrasena = input("Introduce tu contraseña: ")
            iniciar_sesion(usuario, contrasena)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

# Llama a la función principal del programa
if __name__ == "__main__":
    main()
