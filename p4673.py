d = {}
for i in range(10000):
    str_i = str(i)
    l = []
    for j in range(len(str_i)):
        l.append(int(str_i[j]))
    result = int(str_i) + sum(l)
    d[result] = 0
for i in range(10000):
    if(i not in d.keys()):
        print(i)
