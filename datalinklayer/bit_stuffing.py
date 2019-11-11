flag = "01111110"

def en_frame(data):
	frame = ""
	count_1 = 0  
	for k in data:
		if k == "1":
			count_1 += 1
		else:
			count_1 = 0

		if count_1 == 5:
			count_1 = 0
			frame += "10"
		else:
			frame += k
	return flag + frame +flag
	
def de_frame(data):
	i = data[len(flag):-len(flag)]
	
	count_1 = 0
	frame = ""
	for bit in i:
		if count_1 == 5:
			count_1 = 0
			continue
		if bit == "1":
			count_1 += 1
		else:
			count_1 = 0
		frame += bit
	
	return frame