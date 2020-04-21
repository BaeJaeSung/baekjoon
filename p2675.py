n = int(input())
for i in range(n):
    inp = input().split()
    num = int(inp[0])
    inp_str = inp[1]
    res = ''
    for j in range(len(inp_str)):
        for k in range(num):
            res += inp_str[j]
    print(res)
