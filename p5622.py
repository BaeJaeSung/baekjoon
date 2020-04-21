inp = input()
t = 0
for i in range(len(inp)):
    comp = 0
    if(int(ord(inp[i])) >= 83):
        comp = 1
    if(inp[i] == 'Z'):
        comp = 2
    t += int((ord(inp[i])-comp - 62)/3) + 2
print(t)
