a, b, v = map(int, input().split())
a = int(a)
b = int(b)
v = int(v)

n = (v-a)/(a-b)
n = n + 1
if(n == int(n)):
    print(int(n))
else:
    print(int(n+1))

#(a-b)n + a >= v
# n >= (v-b)/(b-a)
