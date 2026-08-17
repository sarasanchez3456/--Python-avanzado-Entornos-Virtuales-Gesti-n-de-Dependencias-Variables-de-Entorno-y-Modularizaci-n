# Gestor de usuarios
usuarios = []


def registrar_usuario(nombre, edad):
    usuario = {
        "nombre": nombre,
        "edad": edad
    }

    usuarios.append(usuario)


def listar_usuarios():
    return usuarios


def buscar_usuario(nombre):
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            return usuario

    return None