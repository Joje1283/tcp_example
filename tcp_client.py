'''
TCP Echo Client
'''

import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 1701))
    sock.send("hello".encode())
    data = sock.recv(65535)
    print("received data : ", data)
