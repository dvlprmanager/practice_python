# client/client.py

import socketio
import time

# Crear una instancia de SocketIO cliente
sio = socketio.Client()

# Evento de conexión
@sio.event
def connect():
    print('Conectado al servidor SocketIO')
    # Enviar un mensaje al servidor después de conectarse
    sio.emit('mensaje_cliente', {'data': 'Hola servidor desde el cliente!'})

# Evento de desconexión
@sio.event
def disconnect():
    print('Desconectado del servidor SocketIO')

# Evento para recibir mensajes del servidor
@sio.on('mensaje_servidor')
def handle_mensaje_servidor(json):
    print('Mensaje del servidor:', json['data'])

def ejecutar_cliente():
    # Conectar al servidor SocketIO
    sio.connect('http://localhost:5000')
    
    # Esperar un poco para recibir mensajes
    time.sleep(1)
    
    # Enviar un mensaje de broadcast
    sio.emit('broadcast_mensaje', {'data': '¡Este es un broadcast a todos los clientes!'})

    # Esperar para recibir el broadcast
    time.sleep(1)
    
    # Desconectar del servidor
    sio.disconnect()

if __name__ == '__main__':
    ejecutar_cliente()
