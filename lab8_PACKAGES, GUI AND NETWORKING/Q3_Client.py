import socket
PORT = 6960
BUFFER_SIZE = 1024

sockfd = socket.socket()
host = socket.gethostname()
sockfd.connect((host,PORT))
string = str(input("Enter the String: "))
sockfd.send(string.encode())
print(sockfd.recv(BUFFER_SIZE).decode())
sockfd.close()

