import sys

def input(): return sys.stdin.readline().strip()
def print(val):return sys.stdout.write(str(val))

def kara(a,b):
    if len(str(a)) == 1 or len(str(b)) == 1:
        return a*b
    else:
        n = max(len(str(a)),len(str(b)))
        k = n // 2
        temp0 = a // 10 ** k
        temp1 = a % 10 ** k
        temp2 = b // 10 ** k
        temp3 = b % 10 ** k

        a = kara(temp0, temp2)
        b = kara(temp1, temp3)
        res = kara(temp1 + temp0, temp3 + temp2) - a - b
        return a * pow(10, k * 2) + res * pow(10, k) + b

n,m = map(int,input().split())
print(kara(n,m))
