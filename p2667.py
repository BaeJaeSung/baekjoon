n = int(input())
arr = []
num_houses = []
ans = 0
num_of_house = 0
for i in range(n):
	a = input()
	temp = []
	for j in range(n):
		temp.append(int(a[j]))
	arr.append(temp)

def find_conjunc(i, j, tf):
	global num_of_house
	global num_houses
	global ans
	if(arr[i][j] == 1):
		if(tf):
			if(num_of_house > 0):
				num_houses.append(num_of_house)
				num_of_house = 0
			ans += 1
		arr[i][j] = 0
		num_of_house += 1
		possible = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
		for elm in possible:
			if(elm[0] < 0 or elm[0] == n or elm[1] < 0 or elm[1] == n):
				pass
			else:
				find_conjunc(elm[0], elm[1], False)
for i in range(n):
	for j in range(n):
		find_conjunc(i, j, True)
if(num_of_house > 0):
	num_houses.append(num_of_house)
num_houses.sort()
print(ans)
for elm in num_houses:
	print(elm)
