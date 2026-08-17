from app.usuarios.gestor import registrar_usuario, listar_usuarios, buscar_usuario
from app.usuarios.validaciones import validar_nombre, validar_edad
from app.config.settings import APP_NAME, APP_VERSION


def mostrar_menu():
    print("**********************************")
    print(f"{APP_NAME} v{APP_VERSION}")
    print("**********************************")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")


def main():

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Registrar usuario ---")

            nombre = input("Nombre: ")

            try:
                nombre = validar_nombre(nombre)

                edad = input("Edad: ")
                edad = validar_edad(edad)

                registrar_usuario(nombre, edad)

                print("Usuario registrado correctamente.")

            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "2":
            print("\n--- Lista de usuarios ---")

            usuarios = listar_usuarios()

            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for usuario in usuarios:
                    print(f"Nombre: {usuario['nombre']} | Edad: {usuario['edad']}")

        elif opcion == "3":
            print("\n--- Buscar usuario ---")

            nombre = input("Ingrese el nombre a buscar: ")

            usuario = buscar_usuario(nombre)

            if usuario:
                print(
                    f"Usuario encontrado: "
                    f"{usuario['nombre']} | Edad: {usuario['edad']}"
                )
            else:
                print("No se encontró ningún usuario.")

        elif opcion == "4":
            print("\nSaliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()