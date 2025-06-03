from flask import Flask, render_template, request, jsonify
from chatbot import obter_resposta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    mensagem = request.json.get('mensagem')
    resposta = obter_resposta(mensagem)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
