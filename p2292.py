num = int(input())
n = 0
while(True):
    target = 1 + int(6 * (n+1) * n / 2)
    if(target >= num):
        print(n + 1)
        break
    n += 1
