import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8089))

print("Servidor conectado")

try:
    print("-------------")
    while True:
        response = client_socket.recv(1024)

        if not response:
            print("Se cerró la conexión.")
            break

        print(f"Server: {response.decode()}")
except ConnectionResetError:
    print("Conexión perdida")
finally:
    client_socket.close()