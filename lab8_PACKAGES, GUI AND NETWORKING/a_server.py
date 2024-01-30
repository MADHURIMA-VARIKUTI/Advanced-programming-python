import socket

def search_number(numbers, target):
    if target in numbers:
        return f"{target} found in the set."
    else:
        return f"{target} not found in the set."

def sort_numbers(numbers, ascending=True):
    numbers.sort()
    if not ascending:
        numbers.reverse()
    return numbers

def split_odd_even(numbers):
    odd_numbers = [x for x in numbers if x % 2 != 0]
    even_numbers = [x for x in numbers if x % 2 == 0]
    return odd_numbers, even_numbers

def handle_client(client_socket):
    print("Connection established with client.")
    
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        
        choice, numbers = data.split(":")
        numbers = list(map(int, numbers.split(",")))

        if choice == "1":
            target = int(input("Enter the number to search: "))
            result = search_number(numbers, target)
        elif choice == "2":
            ascending = input("Sort in ascending order (y/n): ").lower() == 'y'
            result = sort_numbers(numbers, ascending)
        elif choice == "3":
            odd, even = split_odd_even(numbers)
            result = (odd, even)
        else:
            result = "Invalid choice."

        client_socket.send(str(result).encode())

    print("Connection closed with client.")
    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server listening on {}:{}".format(host, port))

    while True:
        client_socket, client_addr = server_socket.accept()
        handle_client(client_socket)

if __name__ == "__main__":
    main()
