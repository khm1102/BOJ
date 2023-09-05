exp = input().split('-')
num = [sum(map(int, i.split('+'))) for i in exp]
result = num[0] - sum(num[1:])
print(result)
