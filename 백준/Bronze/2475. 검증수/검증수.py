a = list(map(int, input().split()))
list = []

for i in range(0, len(a)):
  list.append(a[i]**2)

print(sum(list)%10)