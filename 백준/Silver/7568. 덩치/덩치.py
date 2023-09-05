N = int(input())
people = []  
for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))


rank = [] 
for i in range(N):
    count = 1 
    for j in range(N):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    rank.append(count)

for r in rank:
    print(r, end=' ')
