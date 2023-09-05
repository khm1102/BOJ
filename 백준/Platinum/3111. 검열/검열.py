from collections import deque

a = input();t = input()
F = deque();B = deque()
L = 0;R = len(t) - 1
ans = ""

while L <= R:
    while L <= R:
        F.append(t[L])
        L += 1
        if len(F) >= len(a):
            Flag = all(a[i] == F[-len(a) + i] for i in range(len(a)))
            if Flag:
                for _ in range(len(a)):
                    F.pop()
                break

    while L <= R:
        B.appendleft(t[R])
        R -= 1
        if len(B) >= len(a):
            Flag = all(a[i] == B[i] for i in range(len(a)))
            if Flag:
                for _ in range(len(a)):
                    B.popleft()
                break

ans += "".join(F)
ans += "".join(B)

while a in ans:ans = ans.replace(a, "", 1)
if ans:print(ans)
