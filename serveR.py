import socket
import threading

# Define IP and port
HOST = '127.0.0.1'
PORT = 8888

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        command = data.decode('utf-8')
        if command == "ping":
            response = "pong"
        elif command == "get_time":
            import time
            response = f"Server time: {time.ctime()}"
        else:
            response = "Unknown command"

        client_socket.send(response.encode('utf-8'))
    client_socket.close()

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Server listening on {HOST}:{PORT}")

        while True:
            client_socket, client_addr = server_socket.accept()
            print(f"Accepted connection from {client_addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == '__main__':
    server()
