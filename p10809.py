inp = input()
alpha = [chr(97+i) for i in range(26)]

res = ''
for i in alpha:
    for j in range(len(inp)):
        if(inp[j] == i):
            res += str(j) + ' '
            break
    else:
        res += '-1 '
print(res[:-1])
