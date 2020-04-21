num = int(input())
ans = 0
d = {}

def start(a, b):
	res = 0
	if(a == 0):
		return b
	if(b == 1):
		return 1
	else:
		if("{0},{1}".format(a,b) in d.keys()):
			return d["{0},{1}".format(a,b)]
		for j in range(1, b+1):
			res += start(a-1, j)
		d["{0},{1}".format(a,b)] = res
		return res

	pass

for i in range(num):
	a = int(input())
	b = int(input())
	res = start(a, b)
	print(res)



'''
num = int(input())
ans = 0
d = {}

def start(a, b):
	res = 0
	if(a == 0):
		return b
	if(b == 1):
		return a
	else:
		if("{0},{1}".format(a,b) in d.keys()):
			return d["{0},{1}".format(a,b)]
		for i in range(a):
			for j in range(1, b+1):
				res += start(i, j)
		d["{0},{1}".format(a,b)] = res
		return res

	pass

for i in range(num):
	a = int(input())
	b = int(input())
	res = start(a, b)
	res2 = start(a-1, b)
	print(res-res2)
'''
