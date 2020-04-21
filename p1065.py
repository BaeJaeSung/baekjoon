n = input()
result = 0
for i in range(int(n)):
    adj_i = i + 1
    if(adj_i <= 99):
        result += 1
    else:
        str_i = str(adj_i)
        d = int(str_i[0]) - int(str_i[1])
        for j in range(len(str_i)-1):
            if(d != int(str_i[j]) - int(str_i[j+1])):
                break
        else:
            result += 1
print(result)
