import math
static_cost, variable_cost, price = map(int, input().split())
if(price == variable_cost):
    if(static_cost >= 0):
        print(-1)
    else:
        print(0)
    exit()
num = static_cost/(price-variable_cost)
if(num >= 0):
    print(int(num) + 1)
else:
    print(-1)
