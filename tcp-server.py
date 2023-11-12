#!/usr/bin/env python3
# test5_server

import socket
import time

IP_ADDR = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((IP_ADDR, TCP_PORT))
    s.listen(1)

    print(f"Server listening on {IP_ADDR}:{TCP_PORT}")

    try:
        while True:
            conn, addr = s.accept()
            print('Client address:', addr)
            try:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                currentTime = " " + "updated !!!" + time.ctime(time.time()) + "\r\n"
                data = data.decode('utf-8') + currentTime
                conn.send(data.encode('ascii'))
            except Exception as e:
                print(f"Error handling client: {str(e)}")
            finally:
                conn.close()
    except KeyboardInterrupt:
        print("Server stopped by user")
    finally:
        s.close()

if __name__ == "__main__":
    main()
