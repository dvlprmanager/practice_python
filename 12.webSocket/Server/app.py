# server/app.py

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Inicializar la aplicación Flask y SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_secreto_aqui'
socketio = SocketIO(app, cors_allowed_origins="*")  # Permitir CORS para todas las orígenes

# Ruta principal (opcional, si deseas servir una página web)
@app.route('/')
def index():
    return "Servidor SocketIO está corriendo."

# Evento de conexión
@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')
    emit('mensaje_servidor', {'data': '¡Bienvenido al servidor SocketIO!'})

# Evento de desconexión
@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')

# Evento personalizado: enviar mensaje desde el cliente al servidor
@socketio.on('mensaje_cliente')
def handle_mensaje_cliente(json):
    print('Mensaje del cliente:', json)
    # Responder al cliente
    emit('mensaje_servidor', {'data': 'Mensaje recibido en el servidor.'})

# Evento personalizado: broadcast (difundir) mensaje a todos los clientes
@socketio.on('broadcast_mensaje')
def handle_broadcast(json):
    print('Broadcast mensaje:', json)
    emit('mensaje_servidor', {'data': json['data']}, broadcast=True)

if __name__ == '__main__':
    # Ejecutar el servidor con eventlet
    socketio.run(app, host='0.0.0.0', port=5000)
