import Pyro4

# Configuración de conexión Pyro con el servidor de chat
chat_server = Pyro4.Proxy("PYRO:obj_cb688307b9cd450abf9b343ee5fe2e31@localhost:3303") 

def main():
    while True:
        message1 = input("Escribe un mensaje para enviar al chat: ")
        message2 = "client: " + message1
        chat_server.send_message(message2)
        print("Mensaje enviado al chat.")

if __name__ == "__main__":
    main()
