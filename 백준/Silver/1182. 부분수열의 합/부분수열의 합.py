from itertools import combinations
n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(sum(1 for i in range(1, n+1) for c in combinations(arr, i) if sum(c) == k))