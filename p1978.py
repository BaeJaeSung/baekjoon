n = int(input())
st = input().split()
res = 0
for elm in range(len(st)):
    temp = int(st[elm])
    if(temp == 1):
        continue
    if(temp == 2):
        res += 1
        continue
    for j in range(2, temp):
        if(temp%j == 0):
            break
    else:
        res += 1
print(res)
