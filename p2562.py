d = {}
min = 0
max = 0
for i in range(9):
    inp = int(input())
    if(i==0):
        min = inp
        max = inp
    d[inp] = i+1
    if(inp > max):
        max = inp
    if(inp < min):
        min = inp
print(max)
print(d[max])
