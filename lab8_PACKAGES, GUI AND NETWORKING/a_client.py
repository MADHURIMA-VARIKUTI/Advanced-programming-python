import socket

def send_choice_and_numbers(client_socket, choice, numbers):
    data = f"{choice}:{','.join(map(str, numbers))}"
    client_socket.send(data.encode())

def receive_result(client_socket):
    result = client_socket.recv(1024).decode()
    return result

def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        print("\nChoose an option:")
        print("1. Search for a number")
        print("2. Sort the set")
        print("3. Split odd and even")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "4":
            client_socket.send("4:".encode())
            break

        numbers = list(map(int, input("Enter a comma-separated list of integers: ").split(",")))

        send_choice_and_numbers(client_socket, choice, numbers)
        result = receive_result(client_socket)

        if choice == "1":
            print(result)
        elif choice == "2":
            print(f"Sorted set: {result}")
        elif choice == "3":
            odd, even = result
            print(f"Odd numbers: {odd}")
            print(f"Even numbers: {even}")

    client_socket.close()

if __name__ == "__main__":
    main()
