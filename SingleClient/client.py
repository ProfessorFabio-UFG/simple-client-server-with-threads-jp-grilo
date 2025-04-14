import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

    print("Connected to the server.")
    print("Enter your request in the format: <num1> <operation> <num2>")
    print("Supported operations: add, subtract, multiply, divide")

    while True:
        request = input("Enter request (or 'exit' to quit): ")
        if request.lower() == "exit":
            break

        # Send the request to the server
        client.send(request.encode('utf-8'))

        # Receive the response from the server
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

    client.close()

if __name__ == "__main__":
    main()