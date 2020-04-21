count = 0
n = int(input())
for i in range(n):
    d = {}
    pivot = 1
    word = input()
    character = word[0]
    if(len(word) == 1):
        count += 1
    else:
        while(pivot != len(word)):
            if(word[pivot] == character):
                pivot += 1
            else:
                if(word[pivot] in d.keys()):
                    break
                else:
                    d[word[pivot-1]] = 1
                    character = word[pivot]
                pivot += 1
            if(pivot == len(word)):
                count += 1
print(count)
