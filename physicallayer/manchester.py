def encode(data):
	res = ""
	n=len(data)
	for i in range(n):
		if data[i]=="0":
			res+="01"
		else:
			res+="10"
			
	return res
	
	
def decode(data):
	res = ""
	n=len(data)
	for i in range(0,n,2):
		j=i+2
		bit= data[i:j]
		if bit == "01":
			res+="0"
		else:
			res+="1"
			
	return res