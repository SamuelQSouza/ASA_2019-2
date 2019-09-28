from flask import Flask, url_for, request, json, jsonify

app = Flask(__name__)
@app.route('/')
def api_root():
    return "Seja bem vindo!!"

@app.route('/hello')
def api_hello():
    if 'nome' in request.args:
        return 'olá ' + request.args['nome']
    else:
        return "Olá desconhecido"

@app.route('/hello2')
def api_hello2():
    if 'nome' in request.args:
        return 'olá ' + request.args['nome'] + ' '+ request.args['sobrenome']
    else:
        return "Olá desconhecido"
@app.route('/echo', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"
    
    elif request.method == 'POST':
        return "ECHO: POST\n"
    
    elif request.method == 'PUT':
        return "ECHO: PUT\n"
    
    elif request.method == 'DELETE':
        return "ECHO: DELETE\n"
    

if __name__ == 'main':
    app.run()
