# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *

message = ""
serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = clientSocket.recv(1024).decode()

    # Run this loop if message is not null
    if len(message) > 0:
        print('\nFrom Server: ' + message + '\n')

    # Grabs input from user and sends to server
    # Note: raw_input is used here. Py 3 says it doesn't support it, but it will still work when ran in Mininet
    message = raw_input('Enter message to send to server: ')
    clientSocket.send(message.encode())

    clientSentence = clientSocket.recv(1024).decode('utf-8')
    print('From Server: ' + clientSentence)

clientSocket.close()
