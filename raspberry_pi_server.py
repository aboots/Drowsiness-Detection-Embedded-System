import socket
import asyncio
import sys
from gpiozero import Buzzer
from time import sleep
from gpiozero import AngularServo
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)


servo = AngularServo(4, min_angle=-90, max_angle=90)
servo.angle = 90
buzzer = Buzzer(17)

def handle_run_arguments():
    if len(sys.argv) != 2:
        print("Usage: python server.py <IP>:<PORT>")
        sys.exit(1)

    ip_address, port_number = sys.argv[1].split(":")

    try:
        ip_address = str(ip_address.strip())
        port_number = int(port_number.strip())
    except ValueError:
        print("Invalid input format: expected <IP>:<PORT>")
        sys.exit(1)

    return ip_address, port_number


async def handle_client(client, addr):
    loop = asyncio.get_event_loop()
    await loop.sock_sendall(client,'connected to server'.encode())
    request = None
    request = (await loop.sock_recv(client, 255)).decode('utf8')
    if request != 'ack':
        print('bad connection')
        return
    else:
        print('connectaion established successfully.')
    while True:
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        if request != 'quit':
            print(f'got from {addr} : {request}')
            if request == '1' or request == '2':
                if request == '2':
                    GPIO.output(22, GPIO.HIGH)
                elif request == '1':
                    GPIO.output(5, GPIO.HIGH)
                print('yes')
                servo.angle = -90
                buzzer.on()
                sleep(0.5)
                servo.angle = 90
                buzzer.off()
                if request == '2':
                    GPIO.output(22, GPIO.LOW)
                elif request == '1':
                    GPIO.output(5, GPIO.LOW)
            else:
                print('no')
            response = 'ok'
            await loop.sock_sendall(client, response.encode('utf8'))
        else:
            print(f'close client with address {addr}')
            break
    

async def run_server(ip_address, port_number):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_address, port_number))
    server.listen(8)
    server.setblocking(False)
    print('server binded and ready to listen')

    loop = asyncio.get_event_loop()

    while True:
        client, addr = await loop.sock_accept(server)
        print("connected to client :",addr)
        loop.create_task(handle_client(client, addr))

if __name__ == "__main__":
    ip_address, port_number = handle_run_arguments()  
    asyncio.run(run_server(ip_address, port_number))
