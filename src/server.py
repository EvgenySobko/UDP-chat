import queue
import threading
import socket


def recv_data(sock, recv_packets):
    while True:
        data, addr = sock.recvfrom(1024)
        recv_packets.put((data, addr))


def run_server():
    host = socket.gethostbyname("0.0.0.0")
    port = 9999
    print('Server hosting on IP-> ' + str(host))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    clients = set()
    recvPackets = queue.Queue()

    print('Server Running...')

    threading.Thread(target=recv_data, args=(s, recvPackets)).start()

    while True:
        if recvPackets.not_empty:
            data, addr = recvPackets.get()
            if addr not in clients:
                clients.add(addr)
                continue
            clients.add(addr)
            data = data.decode('utf-8')
            if data.endswith('qqq'):
                clients.remove(addr)
                continue
            print(str(addr) + data)
            for c in clients:
                if c != addr:
                    s.sendto(data.encode('utf-8'), c)
    s.close()


if __name__ == '__main__':
    run_server()
    print('Server is online now!')

