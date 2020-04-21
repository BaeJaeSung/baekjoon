mini = int(input())
maxi = int(input())
res = 0
min_num = 0
for i in range(mini, maxi+1):
    if(i == 1):
        continue
    if(i == 2):
        res += i
        min_num = 2
        continue
    for j in range(2, i):
        if(i%j == 0):
            break
    else:
        if(min_num == 0):
            min_num = i
        res += i
if(res == 0):
    print(-1)
else:
    print(res)
    print(min_num)
