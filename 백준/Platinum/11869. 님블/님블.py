N = int(input())
total = 0
num_li = list(map(int, input().split()))
for num in num_li:
    total ^= num
print('koosaga' if total else 'cubelover')