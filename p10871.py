a, b = map(int, input().split())
l = input().split()
txt = ''
for i in range(a):
    if(int(l[i]) < b):
        txt += '{0} '.format(l[i])
print(txt[:-1])
