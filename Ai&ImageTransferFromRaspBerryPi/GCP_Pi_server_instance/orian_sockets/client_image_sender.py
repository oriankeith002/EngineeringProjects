import cv2
import numpy as np
import socket
import sys
import pickle
import struct

# capture photo
cap = cv2.VideoCapture(0)

if cap:
    ret,img = cap.read()
    cv2.imwrite('TransitPhoto.png',img)
    cap.release()
    cv2.destroyAllWindows()

# read photo
file = open('TransitPhoto.png','rb')
image_data = file.read(2048)


# connect to server
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('34.134.96.236',8089))
print('Connection Established')

# send photo to server
while True:
    clientsocket.send(image_data)
    image_data = file.read(2048)
    print ('Image was successfully transmitted')

file.close()
clientsocket.close()

