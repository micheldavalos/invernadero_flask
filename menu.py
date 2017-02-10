from prueba import administrador
# comentario
'''
    multiples
'''
class menu():
    def mostrar(self):
        print("1) Agregar usuarios")
        print("2) Mostrar")
        print("0) Salir")
        op = input()

        return op

    def agregar_usuario(self):
        nombre = input("Nombre: ")
        apellido1 = input("Apellido: ")
        apellido2 = input("Apellido 2:")
        correo = input("Correo: ")
        password = input("Password: ")
        tipo = input("Tipo: ")
        tipo = int(tipo)

        return [nombre, apellido1, apellido2, correo, password, tipo]
