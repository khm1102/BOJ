n = input();a = set(map(int, input().split()));b = set(map(int, input().split()));res = sorted(a.difference(b))
print(len(res), *res)