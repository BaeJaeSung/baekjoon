num = int(input())
ans = 0
for i in range(num):
	a, b = map(int, input().split())
	a = int(a)
	b = int(b)
	dist = b-a
	current_dist = 1
	while(True):
		if(dist <= current_dist):
			ans += 1
			dist = dist - current_dist
		else:
			dist = dist - current_dist * 2
			ans += 2
		if(dist <= 0):
			break
		#print(dist, current_dist)
		current_dist += 1
	print(ans)
	ans = 0
