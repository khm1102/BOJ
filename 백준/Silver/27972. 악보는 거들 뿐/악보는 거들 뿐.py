n = int(input())
s = list(map(int, input().split()))
ans = down = up = 0

for i in range(1, n):
    if s[i] > s[i-1]:
        down = 0
        up += 1
        ans = max(ans, up)
        
        
    elif s[i] < s[i-1]:
        down += 1
        up = 0
        ans = max(ans, down)

print(ans+1)
