def count_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 1 + count_ways(n - 1)
    if n == 3:
        return 1 + count_ways(n - 1) + count_ways(n - 2)
    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


t = int(input())  

for _ in range(t):
    n = int(input()) 
    ways = count_ways(n)
    print(ways)