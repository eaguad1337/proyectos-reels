import socket


print("Iniciando servidor...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8089))
server_socket.listen(5)

while True:
    print("Esperando clientes")
    client_socket, client_address = server_socket.accept()
    print(f"Conexión desde {client_address}")

    try:
        while True:
            message = input("Escribe: ")
            client_socket.send(message.encode())

    except Exception as e:
        print(f"Cliente {client_address} desconectado")
    finally:
        client_socket.close()
        server_socket.close()
