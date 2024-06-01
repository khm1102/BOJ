import sys


input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = list(map(int, data[1:n+1]))

arr.sort(reverse=True)

for num in arr:
    print(num)


