def is_prime(num):
    return num>1 and all(num%i for i in range(2,int(num**0.5)+1))

def solve(s1, s2):
    d = 0
    match = [0] * 26

    for i, j in enumerate(s2):
        match[ord(j) - ord('a')] |= 1 << i

    for j in s1:
        x = match[ord(j) - ord('a')] | d
        y = (d << 1) | 1
        d = x ^ (x & (x - y))

    return bin(d).count('1')

s, t, x, y = input(), input(), input(), input()
s, t = map(lambda z: z.replace(y, ''), (s, t))
pos_s, pos_t = map(lambda z: z.find(x), (s, t))

s1, s2 = s.split(x, 1) if pos_s != -1 else (s, "")
t1, t2 = t.split(x, 1) if pos_t != -1 else (t, "")

ret1, ret2 = map(lambda s, t: solve(s, t), (s1, s2), (t1, t2))
print(next((i for i in range(ret1 + ret2 + 1, -1, -1) if is_prime(i)), -1))
