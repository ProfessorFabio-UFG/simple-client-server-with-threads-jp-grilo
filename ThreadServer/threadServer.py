import socket
import threading

def handle_client(client_socket, addr):
    try:
        print(f"Thread iniciada para o cliente {addr}")
        # Receive the request from the client
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request from {addr}: {request}")

        # Parse the request
        parts = request.split()
        if len(parts) != 3:
            response = "Error: Invalid request format. Use: <num1> <operation> <num2>"
        else:
            num1, operation, num2 = parts
            try:
                num1 = float(num1)
                num2 = float(num2)

                # Perform the requested operation
                if operation == "add":
                    result = num1 + num2
                elif operation == "subtract":
                    result = num1 - num2
                elif operation == "multiply":
                    result = num1 * num2
                elif operation == "divide":
                    if num2 == 0:
                        response = "Error: Division by zero is not allowed."
                    else:
                        result = num1 / num2
                else:
                    response = "Error: Unsupported operation. Use: add, subtract, multiply, divide."
                if 'result' in locals():
                    response = f"Result: {result}"
            except ValueError:
                response = "Error: Invalid numbers provided."
        
        # Send the response back to the client
        client_socket.send(response.encode('utf-8'))
    finally:
        print(f"Encerrando conexão com {addr}")
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("ThreadServer listening on port 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        # Create a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    main()