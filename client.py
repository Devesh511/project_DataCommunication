import socket
from datalinklayer.reciever import decodedata
from datalinklayer.bit_stuffing import de_frame
from networklayer.bit_conv import bits2str
from physicallayer.manchester import decode

HOST = '127.0.0.1'
PORT = 65431

with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	while True:
		data = s.recv(1024)
		if data:
			d0=data.decode("utf-8")
			print("Recieved manchester data "+d0)
			d3=decode(d0)
			print("recieved data after manchester decoding "+d3)
			d1=decodedata(d3,"1001")
			if d1=="000":
				print("No Error is dected")
				d2=d3[:-3]
				print("message beforedecoding bit-stuffing "+d2)
				d=de_frame(d2)
				d2=d
				data=bits2str(d2)
			else:
				data="error"
				
			print(data)
			