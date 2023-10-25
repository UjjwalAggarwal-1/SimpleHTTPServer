import socket


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 2450

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f'Listening on port {SERVER_PORT} ...')

while True:    
    try:
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        request = client_connection.recv(1024).decode()
        if not request:
            continue
        print(request)

        # Parse HTTP headers
        # headers = request.split('\n')[0]
        # print(headers)

        content = "wohoo!"
        # response = 'HTTP/1.0 200 OK\n\n' + content
        response = content

        # Send HTTP response
        client_connection.sendall(response.encode())
        client_connection.close()

    except KeyboardInterrupt:
        print("\nClosing server...")
        break

    except Exception as e:
        print(e)
        continue

# Close socket
server_socket.close()