
import socket

HOST = "127.0.0.1"
PORT = 65432

#AF_INET -> address fam for IPv4
#SOCK_STREAM -> TCP protocol... ordered data receiving protocol.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # sock.socket() creates socket object
    # sock.socket() -> don't need to sock.close() later..
    
    # bind() accepts HOST, PORT b/c AF_INET is the addr fam of socket
    sock.bind((HOST, PORT))
    sock.listen()

    connect, addr = sock.accept()

    with connect:
        print(f"Connected by {addr}")
        while True:
            data = connect.recv(1024)
            if not data:
                break

            connect.sendall(data)
