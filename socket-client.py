import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8089))

print("Servidor conectado")

try:
    while True:
        print("Esperando datos.")
        response = client_socket.recv(1024)

        if not response:
            print("Se cerró la conexión.")
            break

        mensaje = response.decode()
        if mensaje == 'apagar':
            break

        print(f"Recibido: {response.decode()}")
except ConnectionResetError:
    print("Conexión perdida")
finally:
    client_socket.close()