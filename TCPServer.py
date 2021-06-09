# Group 4: Trinidad Ramirez, Jerridan Bonbright, Illia Sapryga, Christopher Flores
# Team Programming Assignment 3
# CST 311
# TCPServer.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *
from threading import Thread
import threading

threads = []  # Store threads
clientNames = [] # Store client names
msgsRcvd = [] # Store received messages
connectionCount = 0
programComplete = False # Indicates when the program is complete

serverName = '127.0.0.1'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))

# -> Begin thread class
class ClientThread(threading.Thread):
    # Constructor for threads
    def __init__(self, ip, port, clientName):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientName = clientName
        # Used for debugging purposes to ensure separate threads are created
        # print("Thread started for " + ip)

    # Run func for thread
    def run(self):
        while True:
            # For debugging purposes, determines which thread is being used
            # print("Thread in use is: " + threading.currentThread().getName())

            if len(msgsRcvd) == 1:
                continue

            # Send message to port indicating when messages were received
            elif len(msgsRcvd) >= 2:
                self.port.send((clientNames[0] + ': ' + msgsRcvd[0] + ' received before ' + clientNames[1] + ': ' + msgsRcvd[1]).encode())

            # Decode message from client
            message = self.port.recv(1024).decode()

            # Stores client names, message count, and messages for server responses indicating when messages are received
            clientNames.append(self.clientName)
            msgsRcvd.append(message)
            print("Client " + self.clientName + " sent message " + str(msgsRcvd.index(message) + 1) + ": " + message)

            if len(msgsRcvd) == 2:
                print('\nWaiting a bit for clients to close their connections....')
                print('\nDone.')
                exit()
            
# -> End thread class

print('The server is waiting to receive 2 connections...\n')

# Start listening for connections
while len(threads) < 2:
    serverSocket.listen(2)

    # Accept a connection and create a thread for it
    (connectionSocket, (ip, port)) = serverSocket.accept()
    connectionCount += 1

    # Check if first connection (X) and output
    # Output to server and send to client
    if connectionCount == 1:
        print('Accepted first connection, calling it client X')
        connectionSocket.send('Client X connected'.encode())
        newThreadX = ClientThread(ip, connectionSocket, 'X')
        newThreadX.start()
        threads.append(newThreadX)

    # Check if second connection (Y)
    # Output to server and send to client
    elif connectionCount == 2:
        print('\nAccepted second connection, calling it client Y')
        connectionSocket.send('Client Y connected'.encode())
        newThreadY = ClientThread(ip, connectionSocket, 'Y')
        newThreadY.start()
        threads.append(newThreadY)
        print('\nWaiting to receive messages from client X and client Y...\n')
        programComplete = True

    # Refuse connection if more than 2
    elif connectionCount > 2:
        print('Connection Refused - Maximum of 2\n')
        print('\nWaiting to receive messages from client X and client Y....\n')

# Join threads and close socket if program is complete
if programComplete:
    # Join threads
    for t in threads:
        t.join()

    connectionSocket.close()