from sys import stdin
input = stdin.readline

Max = 1000000

F = [1] * 1000001
G = [0] * 1000001

def calculate_gx():
    for i in range(2, Max + 1):
        for j in range(i, Max + 1, i):
            F[j] += i
    
    for i in range(1, Max + 1):
        G[i] = G[i-1] + F[i]

calculate_gx()

ans = []

T = int(input())
for _ in range(T):
    ans.append(G[int(input())])

print('\n'.join(map(str, ans))+"\n")