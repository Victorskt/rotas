from flask import Flask, render_template

meu_app = Flask(__name__)

@meu_app.route('/abobrinha')
def principal():
    #return '<h2>Retorno da função principal - rota abobrinha</h2>'
    return render_template('abobrinha.html')