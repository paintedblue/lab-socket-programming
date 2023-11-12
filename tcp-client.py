#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket

def main():
    server_ip = input("Server address: ")
    tcp_port = 5005
    buffer_size = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((server_ip, tcp_port))
            print(f"Connected to server {server_ip} on port {tcp_port}.")
            
            while True:
                message = input("Write to server: ")
                if message.lower() == 'bye':  # 'bye' 메시지를 사용하여 종료합니다.
                    print("Closing connection...")
                    s.sendall(message.encode('utf-8'))  # 'bye' 메시지를 서버에게 보냅니다.
                    break
                s.sendall(message.encode('utf-8'))
                print('Sending data:', message)
                data = s.recv(buffer_size)
                print('Data from server:', data.decode('utf-8'))
                if not data:
                    # 데이터 수신이 없으면, 서버가 연결을 닫았다고 가정합니다.
                    print("Server closed the connection.")
                    break

        except socket.error as e:
            print(f"Socket error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # 연결을 정리합니다.
            s.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
