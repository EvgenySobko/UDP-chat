import socket
import threading
import random


def receive_data(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(data.decode('utf-8'))
        except:
            pass


def run_client(ip):
    host = socket.gethostbyname("0.0.0.0")
    port = random.randint(6000, 10000)
    server = (str(ip), 9999)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    name = input('Please write your name here: ')
    if name == '':
        name = 'Guest' + str(random.randint(1000, 9999))
        print('Your name is:' + name)
    s.sendto(name.encode('utf-8'), server)
    threading.Thread(target=receive_data, args=(s,)).start()
    while True:
        data = input()
        if data == 'qqq':
            break
        elif data == '':
            continue
        data = '[' + name + ']' + '->' + data
        s.sendto(data.encode('utf-8'), server)
    s.sendto(data.encode('utf-8'), server)
    s.close()


if __name__ == '__main__':
    run_client('localhost')
