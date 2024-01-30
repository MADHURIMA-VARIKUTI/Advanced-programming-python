import socket

PORT = 6960
sockfd = socket.socket()
host = socket.gethostname()
sockfd.bind((host, PORT))
sockfd.listen(1)

while True:
    client, addr = sockfd.accept()
    print("Connected from", addr)
    String = client.recv(1024).decode()
    length = len(String)
    sstring = 'string is a palindrome'
    ffstring = 'string is not a palindrome'
    if String == String[::-1]:
        client.send(sstring.encode())
    else:
        client.send(ffstring.encode())
    client.close()
