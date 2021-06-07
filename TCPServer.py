#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *
from threading import Thread
import threading

threads = []  # Store threads
clientNames = [] # Store client names
msgsRcvd = [] # Store received messages

port1 = 0
port2 = 0

clientNm = ""

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
    #    print("Thread started for " + ip)

    # Run func for thread
    def run(self):
        while True:
            # For debugging purposes, determines which thread is being used
            # print("Thread in use is: " + threading.currentThread().getName())

            #call certain client port to send message

            if len(msgsRcvd) == 1:
                continue

            #elif len(msgsRcvd) >= 2:
            #    self.port.send((clientNames[0] + ': ' + msgsRcvd[0] + ' received before ' + clientNames[1] + ': ' + msgsRcvd[1]).encode())

            #need a way to get the message port number
            if(len(threads)>=2 and self.port != port1):
                threads[1].port.send(("\nFrom " +self.clientName + ": "+ message).encode('utf-8'))
            if(len(threads)>=2 and  self.port != port2):
                threads[0].port.send(("\nFrom " +self.clientName + ": "+ message).encode('utf-8'))

            # Decode message from client
            message = self.port.recv(1024).decode()

            # Stores client names, message count, and messages for server responses indicating when messages are received
            clientNames.append(self.clientName)
            msgsRcvd.append(message)
            print("Client " + self.clientName + " sent message " + str(msgsRcvd.index(message) + 1) + ": " + message)
# -> End thread class

print('The server is waiting to receive 2 connections...\n')

# Start listening for connections
serverSocket.listen(2)


# Accept connection1 and create a thread for it
(connectionSocket1, (ip1, port1)) = serverSocket.accept()
print('Accepted first connection, calling it client X')
connectionSocket1.send('Client X connected\n'.encode())
newThreadX = ClientThread(ip1, connectionSocket1, 'X')
newThreadX.start()
threads.append(newThreadX)

# Accept connection2 and create a thread for it
(connectionSocket2, (ip2, port2)) = serverSocket.accept()
print('\nAccepted second connection, calling it client Y')
connectionSocket2.send('Client Y connected\n'.encode())
newThreadY = ClientThread(ip2, connectionSocket2, 'Y')
newThreadY.start()
threads.append(newThreadY)
print('\nWaiting to receive messages from client X and client Y...\n')
    # Check if first connection (X) and output
    # Output to server and send to client


    # Check if second connection (Y)
    # Output to server and send to client



    # Refuse connection if more than 2
#elif connectionCount > 2:
#        print('Connection Refused - Maximum of 2\n')
#        print('\nWaiting to receive messages from client X and client Y....\n')

# Join threads
for t in threads:
    t.join()

print('\nWaiting a bit for clients to close their connections....')
connectionSocket.close()
print('\nDone.')
