from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*') # ISSO PERMITE MENSAGENS DE QUALQUER ORIGEM

@socketio.on('message')
def gerenciar_msg(mensagem): #ISSO TUDO SERVE PARA ENVIAR A MENSAGEM
    send(mensagem, broadcast=True)

# criar a primeira rota
@app.route('/')
def homepage():
    return render_template('index.html')

#app.run() # SE ESCREVERMOS (debug=True) DENTRO DE app.run(), ele atualiza automaticamente

socketio.run(app, host='192.168.15.5') #localhost PERMITE QUE O CODIGO SÓ RODE NO SEU COMPUTADOR