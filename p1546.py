a = input()
b = input().split()
for i in range(len(b)):
    b[i] = int(b[i])
b.sort()
for i in range(len(b)):
    b[i] = int(b[i])/int(b[-1]) * 100
sum = 0
for i in b:
    sum += i
print(float(sum)/int(a))
