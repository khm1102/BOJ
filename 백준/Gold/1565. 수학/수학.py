def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

d, m = map(int, input().split())
D = list(map(int, input().split()))
M = list(map(int, input().split()))

vgcd = M[0]  # 최대공약수
for i in range(1, m):
    vgcd = gcd(vgcd, M[i])

vlcm = 1  # 최소공배수
for i in range(d):
    vlcm = lcm(vlcm, D[i])
    if vlcm > vgcd or vlcm == 0:
        print(0)
        exit()

i = 1
cnt = 0
while i * i < vgcd:
    if vgcd % i == 0:
        if i % vlcm == 0:
            cnt += 1
        if (vgcd // i) % vlcm == 0:
            cnt += 1
    i += 1

if i * i == vgcd and (i % vlcm == 0):
    cnt += 1

print(cnt)
