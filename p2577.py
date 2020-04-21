a = int(input())
b = int(input())
c = int(input())

d = {}
for i in range(10):
    d[i] = 0
multi = str(a * b * c)
for j in range(len(multi)):
    d[int(multi[j])] += 1

for k in range(10):
    if(k in d.keys()):
        print(d[k])
    else:
        print(0)
