import math
def f(N,A,B):
    a=math.sqrt(2*A/(N*math.sin(2 * math.pi / N)))
    b=math.sqrt(B/math.pi)
    if a<=b:return N
    else:return int(N*math.asin(b/a)/math.pi)+1
for _ in range(int(input())):
    N,A,B=map(int,input().split())
    print(f(N,A,B))