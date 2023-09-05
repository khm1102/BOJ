import sys
input = sys.stdin.readline

def gcd_r(a,b) :
    if b == 0 :
        return a
    else :
        return gcd_r(b,a%b)

a,b = map(int,input().split())

print('1'*gcd_r(a,b))