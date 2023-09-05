s = input()

a = False
for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        print(len(s))
        exit(0)
    elif i < len(s) - 1 and s[i] != s[i + 1]:
        a = True

if a:
    print(len(s) - 1)
else:
    print(-1)
