from flask import Flask, jsonify
from prueba import administrador
app = Flask('inicio')
admin = administrador()
@app.route('/')
def root():
    data = admin.mostrar_usuarios()
    resp = jsonify(data)
    return resp

app.run()
