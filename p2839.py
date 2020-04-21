# 15*n + k == solve(k) + 3n

kg = int(input())
count = 0
while(kg > 0):
    if(kg % 5 == 0):
        count += int(kg/5)
        break
    else:
        if(kg - 3 >= 0):
            kg -= 3
            count += 1
        else:
            count = -1
            break
if(count == 0):
    count = -1
print(count)
