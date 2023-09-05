s1, k = map(int, input().split())
q = s1 // k;r = s1 % k;n = 1
while k > 0:
    if r > 0:n *= q + 1;r -= 1
    else:n *= q
    k -= 1
print(n)


































