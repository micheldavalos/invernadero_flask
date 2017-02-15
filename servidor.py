from flask import Flask
from prueba import administrador
app = Flask('inicio')

@app.route('/')
def root():
    return "Hola"

app.run()
