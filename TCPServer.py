#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *
import threading

threads = [] # Store threads
num_of_threads = 2
flag = False

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
print('The server is waiting to receive 2 connections....\n')

while len(threads) < 2:
    serverSocket.listen(2)
    connectionSocket, addr = serverSocket.accept()

    if flag == False:
        print('Accepted first connection, calling it client X\n')
        connectionSocket.send('Client X connected\n'.encode())
        flag = True
    else:
        print('Accepted second connection, calling it client Y\n')
        connectionSocket.send('Client Y connected\n'.encode())
        print('Waiting to receive messages from client X and client Y....\n')
