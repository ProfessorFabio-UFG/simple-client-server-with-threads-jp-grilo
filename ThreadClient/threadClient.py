import socket
import threading
import time

def send_request(server_address, request, thread_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)
    print(f"Thread-{thread_id} connected to the server.")

    # Measure the start time
    start_time = time.time()

    # Send the request to the server
    client.send(request.encode('utf-8'))

    # Receive the response from the server
    response = client.recv(1024).decode('utf-8')

    # Measure the end time
    end_time = time.time()

    # Print the response and the time taken
    print(f"Thread-{thread_id} Server response: {response} (Time: {end_time - start_time:.4f} seconds)")

    client.close()

def main():
    server_address = ("127.0.0.1", 9999)

    while True:
        user_input = input("Enter request (or 'exit' to quit, or 'balance test' for 30 requests): ").strip()

        if user_input.lower() == "exit":
            print("Exiting client.")
            break
        elif user_input.lower() == "balance test":
            # Generate 30 requests for the balance test
            requests = [f"{i} add {i+1}" for i in range(30)]
            threads = []

            print("Starting balance test with 30 requests...")
            for i, request in enumerate(requests):
                thread = threading.Thread(target=send_request, args=(server_address, request, i))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            print("Balance test completed.")
        else:
            # Single request mode
            thread = threading.Thread(target=send_request, args=(server_address, user_input, 0))
            thread.start()
            thread.join()

if __name__ == "__main__":
    main()