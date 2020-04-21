n = int(input())
for i in range(n):
    inp = input().split()
    num_of_students = int(inp[0])
    scores = inp[1:]
    avg = 0
    for i in range(len(scores)):
        scores[i] = int(scores[i])
        avg += scores[i]
    avg = avg/num_of_students
    result_num = 0
    for i in scores:
        if(i > avg):
            result_num += 1
    print('{0:0.3f}%'.format(round(result_num/num_of_students * 100, 3)))
