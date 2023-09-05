from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def getPi(P):
    m = len(P)
    j = 0
    pi = [0 for _ in range(m)]
    for i in range(1, m):
        while j > 0 and P[i] != P[j]:
            j = pi[j-1]
        if P[i] == P[j]:
            j += 1
            pi[i] = j
    return pi

def KMP(T, P):
    result = []
    pi = getPi(P)
    n, m = len(T), len(P)
    j = 0
    for i in range(n):
        while j > 0 and T[i] != P[j]:
            j = pi[j-1]
        if T[i] == P[j]:
            if j == m-1:
                result.append(i-m+1)
                j = pi[j]
            else:
                j += 1
    return len(result) > 0

N = int(input())
songs = []
for i in range(N):
    data = list(map(int, input().split()))[1:]
    new_data = [data[i+1] - data[i] for i in range(len(data)-1)]
    songs.append(new_data)
L = int(input())
melody = list(map(int, input().split()))
new_melody = [melody[i+1] - melody[i] for i in range(L-1)]

res = []
for idx, song in enumerate(songs):
    if KMP(song, new_melody):
        res.append(idx+1)

if res:
    for idx in res:
        print(str(idx) + ' ')
else:
    print("-1")
