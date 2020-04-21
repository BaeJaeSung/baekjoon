num = int(input())
ans = 0
for i in range(num):
	a, b, c = map(int, input().split())
	h = int(a)
	w = int(b)
	c = int(c)

	ho = (c-1)%h + 1
	cheung = int((c-1)/h) + 1
	if(cheung <= 9):
		cheung = '0' + str(cheung)
	print(str(ho) + str(cheung))
