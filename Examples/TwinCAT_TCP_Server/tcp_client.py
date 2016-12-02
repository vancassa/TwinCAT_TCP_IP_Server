import socket

s = socket.socket()

host = '127.0.0.1' #IP address of the server
port = 30000

s.connect((host, port))
print("Connected")
while(1):
	dataIn = input('Send: ')
	s.send(bytes(dataIn, 'utf-8'))
	dataOut = s.recv(1024)
	print(dataOut)
