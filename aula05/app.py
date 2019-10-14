from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def homepage():
    title ='ASA!'
    paragraph= 'teste'
    message = 'Funcionou'

    try:
        return render_template('index.html', title = title, paragraph =paragraph, message = message)
    except Exception as e:
        return str(e)

@app.route('/disciplinas')
def disciplinas():
    username = 'João'
    lista_disc = ['iec', 'calc2', 'asa', 'bd']
    dict_disc = {'iec': 45, 'calc2': 45, 'asa': 60, 'bd': 60}
    try:
        return render_template('disciplinas.html', username = username, lista_disc = lista_disc, dict_disc = dict_disc)
    except Exception as e:
        return str(e)

@app.route('/seila')
def seila():
    try:
        return render_template('index2.html')
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = '8080' )