import socket

s = socket.socket()

host = '169.254.28.233' #IP address of the server
port = 30000

s.connect((host, port))
print("connected")

print(s.recv(1024))
s.send(b'out1')
print(s.recv(1024))
s.send(b'out2')
print(s.recv(1024))