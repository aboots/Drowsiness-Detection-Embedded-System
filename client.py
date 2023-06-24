import socket 
import sys  

def handle_run_arguments():
    if len(sys.argv) != 2:
        print("Usage: python client.py <IP>:<PORT>")
        sys.exit(1)

    ip_address, port_number = sys.argv[1].split(":")

    try:
        ip_address = str(ip_address.strip())
        port_number = int(port_number.strip())
    except ValueError:
        print("Invalid input format: expected <IP>:<PORT>")
        sys.exit(1)

    return ip_address, port_number


class Client:

    def __init__(self, ip_address, port_number):
        self.sock = socket.socket()                    
        buff_size = 1500
        self.sock.connect((ip_address, port_number))
        self.sock.send('ack'.encode()) 
        print(self.sock.recv(buff_size).decode())
        print('client is ready')
