#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *

message = ''
serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# x = 0


message = clientSocket.recv(1024).decode()  # utf-8?

    # Run this loop if message is not null
if len(message) > 0:
    print('\nFrom Server: ' + message + '\n')

    # User inputs message
    # Message is sent to Server
message = input('Enter message to send to server: ')
clientSocket.send(message.encode("utf-8"))  # utf-8?

message = clientSocket.recv(1024).decode()
if(len(message) > 0):
    print('\nFrom Server: ' + message + '\n')

    # input("  **For Debug Press Enter to force close**  ")
    # clientSocket.close()
