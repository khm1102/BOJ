N = int(input())
M = int(input())
S = input()

count = 0
pattern = 'I' + 'OI' * N

for i in range(M - len(pattern) + 1):
    if S[i:i+len(pattern)] == pattern:
        count += 1

print(count)
