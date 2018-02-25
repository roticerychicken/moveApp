#Socket client example in python
 
import socket   #for sockets
 
#create an AF_INET, STREAM socket (TCP)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
    
print 'Socket Created'