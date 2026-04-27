s = input()
l = len(s)

res = 2 * l

for i in range(2):
    j = l - 1
    k = l - 1
    
    while j >= i and k >= 0:
        if s[k] == "KSA"[j % 3] and k % 2 == j % 2:
            j -= 1
        k -= 1
    j += 1
    
    if j % 2 != i:
        j += 1
    res = min(res, 2 * j)
    
print(res)
