#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket

IP = input("Server address: ")
TCP_PORT = 5000
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, TCP_PORT))
    print("Connected to server.")
    
    while True:
        MESSAGE = input("Write to server (type 'q' to quit): ")
        if MESSAGE.lower() == 'q':  # Allows 'Q' or 'q' to quit
            break
        s.send(MESSAGE.encode('utf-8'))
        print('Sending data:', MESSAGE)
        data = s.recv(BUFFER_SIZE)
        print('Data from server:', data.decode('utf-8'))

    print("Connection closed.")
