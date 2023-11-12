#!/usr/bin/env python3
# test5
import socket
import time
import threading

IP_ADDR = '0.0.0.0'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def handle_client_connection(client_socket, address):
    print(f'New connection from {address}')
    while True:
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break  # 클라이언트가 연결을 종료한 경우
        currentTime = " " + "updated !!!" + time.ctime(time.time()) + "\r\n"
        data = data.decode('utf-8') + currentTime
        client_socket.send(data.encode('ascii'))
    client_socket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP_ADDR, TCP_PORT))
s.listen(1)
print("Waiting for connections...")

try:
    while True:
        client_conn, client_addr = s.accept()
        client_thread = threading.Thread(target=handle_client_connection, args=(client_conn, client_addr))
        client_thread.start()
except KeyboardInterrupt:
    s.close()
    print("Server stopped by user")
