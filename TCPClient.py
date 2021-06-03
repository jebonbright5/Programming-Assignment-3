#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *

message = ''
serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = clientSocket.recv(1024).decode()

    # Run this loop if message is not null
    if len(message) > 0:
        print('\nFrom Server: ' + message + '\n')

    message = input('Enter message to send to server: ')
    clientSocket.send(message.encode())

clientSocket.close()
