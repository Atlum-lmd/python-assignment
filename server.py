import socket

HOST = "127.0.0.1"
PORT = 65535
windowsFlags = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            dataWin = conn.recv(8192, windowsFlags)
            if not dataWin:
                break
            print("dataWin =", dataWin.decode('UTF-8'))
            continue