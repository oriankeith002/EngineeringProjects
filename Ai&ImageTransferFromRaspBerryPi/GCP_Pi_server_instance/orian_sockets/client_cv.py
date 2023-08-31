import cv2
import numpy as np
import socket
import sys
import pickle
import struct 


cap = cv2.VideoCapture(0)
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('34.134.96.236',8089))
print('Connection Established')
while True:
    while(cap.isOpened()):
        ret,frame = cap.read()
        data = pickle.dumps(frame)
        message = struct.pack("Q",len(data)) + data
        clientsocket.sendall(message)
        print('Transmitting video')
        clientsocket.close()
        #cv2.imshow('Transmitting video data',frame)
#        key = cv2.waitKey(1) & 0xFF
#        if key==ord('q'):
#           clientsocket.close()

