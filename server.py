from socket import *
from threading import Thread 

def clientHandler():
	conn, addr = s.accept()
	print addr, "is connected"
	while 1:
		data = conn.recv(1024)
		if not data:
			break
		print "Recieved Message", repr(data)
		conn.send(data);

HOST = ''
PORT = 8002
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

print "Server is running"

for i in range(5):
	Thread(target=clientHandler).start()

s.close()






'''import socket
import sys

host = ''
port = 5545
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((host,port))
except socket.error as e:
	print(str(e))
s.listen(5)

def threaded_client(conn):
	conn.send(str.encode('Welcome,type message'));

	while True:
		data = conn.recv(2048)
		reply = 'Server output: ' + data.decode('utf-8')
		if not data:
			break
		conn.sendall(str.encode(reply))
	conn.close()

while True:
	conn, addr = s.accept()
	print('connected to: ' + addr[0] + ':' + str(addr[1]))
'''


