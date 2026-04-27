n = int(input())
li = list(map(int, input().split()))
k = int(input())

f = (lambda n, li, m: 
                    (li[0] % m) if n == 0 else
                    (pow(li[1], li[0], m) if n == 1 else
                    (pow(li[2], pow(li[1], li[0], m - 1) + m - 1, m))))
print(f(n, li, k))