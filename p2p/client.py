import socket

# Define socket host and port
SERVER_HOST = '172.17.52.143'
SERVER_PORT = 2450

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    client_socket.connect((SERVER_HOST,SERVER_PORT))
    message = b"Hello from client!"
    while True:
        client_socket.send(message)
        data = client_socket.recv(1024)
        print(data.decode())
        message = input("-->").encode()

except KeyboardInterrupt:
    print("\nClosing client...")

except Exception as e:
    print(e)

# Close socket
client_socket.close()