R, C = map(int, input().split())
Str = []
for _ in range(R):
    S = input()
    Str.append(list(S))

Vec = []
for i in range(C):
    S = ""
    for j in range(R):
        S += Str[j][i]
    Vec.append(S[1:])

Answer = 0

for _ in range(R - 1):
    SET = set()
    Flag = True
    for j in range(len(Vec)):
        if Vec[j] not in SET:
            SET.add(Vec[j])
        else:
            Flag = False
            break
    if Flag:
        for j in range(len(Vec)):
            Vec[j] = Vec[j][1:]
        Answer += 1
    else:
        break

print(Answer)
