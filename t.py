from random import random
#import modul as m

rows = int(input())
cols = int(input())
arr = []; MaxR = [];
MaxRow = -1; MaxCol = -1; locMaxR = 0; locMaxC = 0;
for i in range(rows):
	arr.append([])
	for j in range(cols):
		arr[i].append(int(random()*10))

for i in range(rows):
	s = 0
	for j in range(cols):
		s += arr[i][j]
	locMaxC = s
	if locMaxC > MaxCol:
		MaxCol = locMaxC
		IDcol = i	
	s = 0

	for i in range(cols):
		s2 = 0
		for j in range(rows):
			s2 += arr[j][i]
		locMaxR = s2
		if locMaxR > MaxRow:
			MaxRow = locMaxR
			IDrow = j
		s2 = 0	

for p in range(rows):
	print(arr[p])
print("Max colum is:", MaxCol,"  ID is: ", IDcol+1)
print("Max row is:", MaxRow,"  ID is: ", IDrow)
