n = int(input())
arr = list(map(int, input().split()))

l = 0;r = n - 1;ans = 0
while l < r:
    re = min(arr[l], arr[r])
    ans = max(ans, (r - l - 1) * re)
    
    if arr[l] < arr[r]:
        l += 1
    else:
        r -= 1

print(ans)
