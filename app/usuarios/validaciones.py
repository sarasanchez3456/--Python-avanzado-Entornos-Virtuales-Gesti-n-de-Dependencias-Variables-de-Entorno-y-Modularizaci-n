# Validaciones de usuarios
def validar_nombre(nombre):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")

    return nombre.strip()


def validar_edad(edad):
    try:
        edad = int(edad)
    except ValueError:
        raise ValueError("La edad debe ser un número entero.")

    if edad < 1:
        raise ValueError("La edad debe ser mayor que 0.")

    return edad