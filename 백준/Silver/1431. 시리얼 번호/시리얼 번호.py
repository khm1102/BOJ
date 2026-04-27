def k_sum(s):
    return sum(int(d) for d in s if d.isdigit())

n = int(input())
s = [input().strip() for _ in range(n)]
s.sort(key=lambda x: (len(x), k_sum(x), x))
print(*s, sep='\n')
