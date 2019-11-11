from random import choice, randint

error= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,3]

def error_generator(data):
	n= choice(error)
	m=len(data)
	if n == 0:
		return data
		
	pos=[]
	res=""
	for i in range(n):
		pos.append(randint(0,m))

	for i in range(m):
		if i in pos:
			if data[i] == "0":
				res+= "1"
			else:
				res+= "0"
		else:
			res+=data[i]
	return res