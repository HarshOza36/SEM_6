import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    n=int(input("Enter value of n:"))
    g=int(input("Enter value of g:"))
    x=int(input("Enter value of x:"))
    A=(g**x)%n
    message = str(A)  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal
        k1=(int(data)**x)%n
        print("K1=",k1)
        message = input(" -> ")  # again take input
        
        
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
