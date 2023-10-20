import socket
import time

# Define IP and port
HOST = '127.0.0.1'
PORT = 8888

def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        while True:
            message = input("Enter a command ('ping', 'get_time', or 'exit'): ")
            
            if message == "exit":
                break

            start_time = time.time()  # Record the time before sending
            client_socket.sendall(message.encode('utf-8'))

            data = client_socket.recv(1024)
            end_time = time.time()  # Record the time upon receiving
            rtt = end_time - start_time  # Calculate RTT

            print(f"Received: {data.decode('utf-8')}")
            print(f"RTT: {rtt:.6f} seconds")

if __name__ == '__main__':
    client()
