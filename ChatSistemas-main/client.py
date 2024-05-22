from flask import Flask, render_template, request, redirect, url_for
import Pyro4

app = Flask(__name__)

# Configuración de conexión Pyro con el servidor de chat
#ipxx ="192.168.1.82"
chat_server = Pyro4.Proxy("PYRO:obj_06bf81992ec84f989a18ceebf3af81ad@192.168.102.29:49781")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    message1 = request.form['message']
    if message1.strip():  # Verificar que el mensaje no esté vacío
        message2 = "client: " + message1
        chat_server.send_message(message2)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
