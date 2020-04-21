n = input()
origin = n
a = 0
b = 0
iters = 0


while(True):
    # n = int(n)
    # n = str(n)
    iters += 1
    if(len(n) == 1):
        a = 0
        b = int(n)
    else:
        a = int(n[0])
        b = int(n[1])
    new_calc = str(a + b)[-1]
    new_calc = str(b) + new_calc
    new_calc = str(int(new_calc))
    if(new_calc == origin):
        print(iters)
        break
    else:
        n = new_calc
