inp = input().split()
a = inp[0][::-1]
b = inp[1][::-1]
if(int(a) > int(b)):
    print(a)
else:
    print(b)
