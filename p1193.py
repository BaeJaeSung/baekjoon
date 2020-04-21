n = int(input())
remained = 0
line = 0
while(True):
	line += 1
	pivot = (line+1) * line / 2
	if(pivot >= n):
		remained = pivot - n + 1
		break

sumed = line + 1
numerator = sumed - remained
if(line%2 == 0):
	print('{0}/{1}'.format(int(numerator), int(sumed-numerator)))

elif(line%2 == 1):
	print('{0}/{1}'.format(int(sumed-numerator), int(numerator)))
