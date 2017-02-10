import sqlite3

class administrador():
    db = sqlite3.connect('invernadero.db')
    c = db.cursor()

    def insert_usuario(self, lista):
        self.c.execute("INSERT INTO usuario(nombre, apellido1, apellido2,  \
                   correo, password, tipo) VALUES(?,?,?,?,?,?)", \
                   (lista[0], lista[1], lista[2], lista[3], lista[4], \
                   lista[5],) )
        self.db.commit()

    def mostrar_usuarios(self):
        self.c.execute("SELECT * FROM usuario")
        for e in self.c:
            print(e)


mostrar_usuarios()
insert_usuario(['michel2', 'ap', 'ap_2', 'a@yahoo.com', '1', 0])
mostrar_usuarios()
