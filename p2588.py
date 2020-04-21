a = int(input())
b = input()
#b1, b2, b3 = [b[i] for i in range(3)]
for i in range(3):
    print(a*int(b[2-i]))
print(a*int(b))
