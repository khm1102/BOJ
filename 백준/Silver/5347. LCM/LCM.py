for i in range(int(input())):
    a,b = map(int,input().split())
    A,B = a,b
    while a!=0:
        b = b%a
        a,b = b,a
    g = b
    l = A * B //b
    print(l)