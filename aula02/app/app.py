from flask import Flask, url_for, request, json, jsonify
from user import User
from json import dumps

app = Flask(__name__)
myUser = []

@app.route('/')
def api_root():
    return "Seja Bem Vindo!!!"

@app.route('/createuser')
def api_createuser():
    global myUser
    myUser.append(User(1, "Joao", 12, "São Paulo"))
    myUser.append(User(2, "Pedro", 13, "São Tome"))
    myUser.append(User(3, "Jorge", 14, "São Bernardo"))
    myUser.append(User(4, "Valdir", 11, "São Roque"))
    myUser.append(User(5, "Antonio", 10, "São Cristovao"))
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/adduser', methods = ['POST'])  #curl --header "Content-Type: application/json"  --request POST  --data '{"username":"tutorials","password":"secret"}'  http://localhost:5000/users
#curl -d '{"id": "6", "nome": "Zezinho", "idade": "15", "cidade": "Uberlandia"}' -H "Content-Type: application/json" -X POST http://localhost:5000/updateuser
def api_newuser():
    global myUser
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']
    new_user = User(id, nome, idade, cidade)
    myUser.append(new_user)
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/listusers', methods = ['GET'])
def api_listusers():
    payload = []
    content = {}
    
    for elem in myUser:        
        content = {'id': str(elem.getUserId()),'[nome]': elem.getUserNome(), '[idade]': str(elem.getUserIdade()), '[cidade]': elem.getUserCidade()}
        payload.append(content)
        content = {}

    res =  json.dumps(payload)       
    
    return jsonify(UserList=res)

@app.route('/getuser', methods = ['GET']) #curl --header "Content-Type: application/json"  --request GET  --data '{"codigo":"1"}'  http://localhost:5000/getuser
def api_getuser():
    global myUser
    user_data = request.get_json() # 
    print(user_data)
    codUser = user_data['codigo']
    print(codUser)
    print(myUser[0].getUserNome())
    res = {'status': 'usuario nao encontrado'}
    for elem in myUser:
        if(int(codUser) == elem.getUserId()):
            res = {'nome': elem.getUserNome()

if __name__ == 'main':
    app.run()
