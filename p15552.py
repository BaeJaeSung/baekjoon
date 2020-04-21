import sys

num = int(input())
for i in range(num):
    two_nums = sys.stdin.readline().rstrip().split()
    print(int(two_nums[0]) + int(two_nums[1]))
    
