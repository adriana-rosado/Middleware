import Pyro4

# Definir la clase del servidor Pyro
@Pyro4.expose
class ChatServerPyro:
    def __init__(self):
        self.clients = []

    def register_client(self):
        client = Pyro4.current_context.client
        self.clients.append(client)

    def send_message(self, message):
        print("Mensaje recibido en el servidor:", message)

    def send_image(self, image_data):
        print("Datos de imagen recibidos en el servidor Pyro:", image_data[:50])

# Iniciar el servidor Pyro
daemon = Pyro4.Daemon()
uri = daemon.register(ChatServerPyro())

print("URI del servidor Pyro:", uri)

daemon.requestLoop()
