import socket
import data

HOST = "127.0.0.1"
PORT = 65535
windowsFlags = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.send(bytes(data.getCpuUsage(), encoding='UTF-8'), windowsFlags)