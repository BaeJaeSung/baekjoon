n = int(input())
txt = input().split()
min = int(txt[0])
max = int(txt[0])
for i in txt:
    num = int(i)
    if num < min:
        min = num
    if num > max:
        max = num
print('{0} {1}'.format(min, max))
