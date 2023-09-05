s = input()
a = 10001

if s[0] == 'x':
    a = 1
elif s[0] == '-' and s[1] == 'x':
    a = -1
elif 'x' not in s:
    a = 0

if a != 10001:
    print(a)
else:
    x = s.index('x')
    ans = ""
    for i in range(x - 1, -1, -1):
        if s[i] == '+' or s[i] == '-':
            ans = s[i] + ans
            break
        ans = s[i] + ans
    print(ans)
