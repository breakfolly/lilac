#-*- coding:utf-8 -*-
import socket

def print_test():
    print ("Hello from Python Function \'print_test\'")

def print_test2(arg1="text"):
    print (arg1)

class LilacServer():
    def __init__(self, host, port, name):
        self.host = host
        self.port = int(port)
        self.name = name
        self.addr = (self.host, self.port)

        self.size = 1024
        self.print_info()
        self.open_server()
    
    def print_info(self):
        print(self.host, self.port, self.name)

    def open_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(self.addr)
            server_socket.listen()

            while True:
                client_socket, client_addr = server_socket.accept()
                msg = client_socket.recv(self.size)
                print ("[{}] msg : {}".format(client_addr, msg))

                client_socket.sendall("welcome!".encode())
                client_socket.close()

class LilacClient():
    def __init__(self, host, port, name):
        self.host = host
        self.port = int(port)
        self.name = name
        self.addr = (self.host, self.port)

        self.size = 1024
        self.print_info()
        self.send_msg()
    
    def print_info(self):
        print(self.host, self.port, self.name)

    def send_msg(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(self.addr)
            client_socket.send("hi".encode())
            msg = client_socket.recv(self.size)
            print ("resp from server : {}".format(msg))
