from flask import Flask
from prueba import administrador
app = Flask('inicio')
admin = administrador()
@app.route('/')
def root():
    print(admin.mostrar_usuarios())
    return "Hola"

app.run()
