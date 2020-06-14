import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.105.76.166', 1235))

new_msg = True
msglen = None

try:
    while True:
        full_msg = ''
        new_msg = True
        while True:
            msg = s.recv(16)
            if new_msg:
                print(f'New message length: {msg[:HEADERSIZE]}')
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg.decode('utf-8')

            if len(full_msg) - HEADERSIZE == msglen:
                print('Full message: ' + full_msg[HEADERSIZE:])
                new_msg = True
                full_msg = ''

finally:
    s.close()
