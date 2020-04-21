n = int(input())
for i in range(n):
    sum = 0
    prev_num = 0
    inp = input()
    for j in range(len(inp)):
        if(inp[j] == 'O'):
            sum += prev_num + 1
            prev_num += 1
        else:
            prev_num = 0
    print(sum)
