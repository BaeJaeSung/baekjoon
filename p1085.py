x, y, w, h = map(int, input().split())
min = w+h + 100

k = x-w
if(k >= 0 and k <min):
	min = k
k = -k
if(k >= 0 and k <min):
	min = k
k = y-h
if(k >= 0 and k <min):
	min = k
k = -k
if(k >= 0 and k <min):
	min = k
if(x >= 0 and x < min):
	min = x
if(y >= 0 and y < min):
	min = y
print(min)
