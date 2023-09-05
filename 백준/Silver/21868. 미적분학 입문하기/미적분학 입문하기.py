import sys

num = input().split()
num2 = input().split()
num3 = int(input())
print(int(num2[0]) * num3 + int(num2[1]))

if int(num2[0]) == 0:
    print("0 0")
else:
    print(num[0], int(num[1]) * abs(int(num2[0])))
