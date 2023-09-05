
n = int(input())
member = []
for i in range(n):
    member.append(input().split())
member.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(member[i][0], member[i][1])
