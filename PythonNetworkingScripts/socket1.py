import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.html HTTP/1.0\r\n\r\n'.encode() #this is a command
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1: #stop program if data is less than 1 byte
        break 
    print(data.decode(), end='') # decode the data

mysock.close() # closing the connection.

# this is how we talk to sockets in python