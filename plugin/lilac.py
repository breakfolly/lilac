#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import socket
import argparse

parser = argparse.ArgumentParser(description='Start a Lilac server.')
parser.add_argument('port', type=int, nargs='?', help='Port number to run on')
parser.add_argument('name', type=str, nargs='?', help='Your name to run on')

class LilacServer():
    def __init__(self, port, name):
        self.host = "127.0.0.1"
        self.port = int(port)
        self.name = name
        self.addr = (self.host, self.port)

        self.size = 1024
        self.isConnected = True
        self.print_info()
        self.open_server()
    
    def print_info(self):
        print(self.host, self.port, self.name)

    def open_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(self.addr)
            server_socket.listen()

            while self.isConnected:
                client_socket, client_addr = server_socket.accept()
                msg = client_socket.recv(self.size)
                print ("[{}] msg : {}".format(client_addr, msg))

                client_socket.sendall("welcome!".encode())
                client_socket.close()

    def quit(self):
        self.isConnected = False

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

if __name__ == '__main__':
    args = parser.parse_args()
    print (args)
    Server = LilacServer(args.port, args.name)
