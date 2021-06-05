#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *
from threading import Thread
import threading

tlock = threading.Lock()
threads = []  # Store threads
num_of_threads = 2

connectionCount = 0

terminate = False

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

# number of messages
numMess = 0
# ------- Start Thread Class -------
class ClientThread(threading.Thread):

    # Constructor for threads
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port


    # Run func for thread
    def run(self):
        firstM =0

        tlock.acquire()
        message = connectionSocket.recv(1024).decode()

        if(threading.currentThread().getName() == "Thread-1"):
            print("Client X sent message 1 : "+ message)
            connectionSocket.send('X: First message received before Y: '.encode()+message.encode())
        else:
            print("Client Y sent message 1 : "+ message)
            connectionSocket.send('Y: First message received before X: '.encode()+message.encode())
        tlock.release()

        if connectionCount >= 2:
            terminate = True

# ------- End Thread Class -------


print('The server is waiting to receive 2 connections...\n')

# Start listening for connections
while True:
    serverSocket.listen(2)

    # Accept a connection and create a thread for it
    (connectionSocket, (ip, port)) = serverSocket.accept()
    connectionCount += 1
    newThread = ClientThread(ip, port)

    # Check if first connection (X) and output
    # Output to server and send to client
    if connectionCount == 1:
        print('Accepted first connection, calling it client X\n')
        connectionSocket.send('Client X connected\n'.encode())

    # Check if second connection (Y)
    # Output to server and send to client
    elif connectionCount == 2:
        print('Accepted second connection, calling it client Y\n')
        connectionSocket.send('Client Y connected\n'.encode())
        print('Waiting to receive messages from client X and client Y...\n')

    elif connectionCount > 2:
        print('Connection Refused - Maximum of 2\n')


    newThread.start()
    threads.append(newThread)

if terminate:
        print('* joining threads *')
        for t in threads:
            t.join()
