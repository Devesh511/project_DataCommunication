import socket
import sys
from datalinklayer.sender import encodedata
from datalinklayer.bit_stuffing import en_frame
from networklayer.bit_conv import str2bits
from physicallayer.error_gen import error_generator
from physicallayer.manchester import encode

HOST = '127.0.0.1'
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn, addr = s.accept()
	
	with conn:
		print('connected by', addr)
		while True:
			print("Enter the string you want to send")
			data=sys.stdin.readline()
			d1=str2bits(data)
			#print(d1)
			d=en_frame(d1)
			d1=d
			print("message after bit-stuffing "+d1)
			d2=encodedata(d1,"1001")
			print("crc encoded data "+d2)
			d3=error_generator(d2)
			data=encode(d3)
			print("Manchester encoded data "+data)
			b1 = bytes(data, encoding = 'utf-8')
			conn.send(b1)