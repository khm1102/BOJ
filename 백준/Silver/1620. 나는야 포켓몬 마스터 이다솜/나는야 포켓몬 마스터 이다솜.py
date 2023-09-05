n, m = map(int, input().split())

pokemon = {}
name = []

for i in range(1, n+1):
    temp = input()
    name.append(temp)
    pokemon[temp] = i

result = []

for i in range(m):
    temp = input()
    if temp[0].isupper():
        result.append(str(pokemon[temp]))
    else:
        result.append(name[int(temp)-1])

for r in result:
    print(r)
