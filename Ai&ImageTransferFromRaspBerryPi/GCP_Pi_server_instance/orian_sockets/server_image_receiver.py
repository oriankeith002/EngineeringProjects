import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new

HOST=''
PORT=8089

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

file = open('received_image_3.jpg','wb')
image_chunk = conn.recv(2048)


while image_chunk:
    file.write(image_chunk)
    image_chunk = conn.recv(2048)
    print(' Image received successfully')
file.close()
conn.close()
