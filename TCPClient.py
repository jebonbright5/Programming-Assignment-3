# Group 4: Trinidad Ramirez, Jerridan Bonbright, Illia Sapryga, Christopher Flores
# Team Programming Assignment 3
# CST 311
# TCPClient.py
# Why is multithreading needed to solve this assignment? 
# Incorporating multiple threads in the program creates parallel execution, which
# is significantly more efficient with regards to program performance. Multithreading
# gives the server the ability to multi-task, and it allows various clients to
# connect to it simultaneously. One of the goals with multi-threading is to ensure
# program flow optimization. Some operations like send() can hinder the program's
# performance without multi-threading

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

    # Decode nessage and print to console
    clientSentence = clientSocket.recv(1024).decode('utf-8')
    print('From Server: ' + clientSentence)

clientSocket.close()