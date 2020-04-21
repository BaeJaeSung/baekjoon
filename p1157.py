inp = input().lower()
d = {}
for i in range(len(inp)):
    if(inp[i] not in d):
        d[inp[i]] = 1
    else:
        d[inp[i]] += 1
max_num = 0
max_char = []
for key in d.keys():
    if(max_num < int(d[key])):
        max_num = int(d[key])
        max_char = [key]
    elif(max_num == int(d[key])):
        max_char.append(key)
if(len(max_char) > 1):
    print('?')
else:
    print(max_char[0].upper())
