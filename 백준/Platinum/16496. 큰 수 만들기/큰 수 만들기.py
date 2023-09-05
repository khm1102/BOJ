from functools import cmp_to_key

def solution():
    N = int(input())
    nums = list(map(str, input().split()))

    nums.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))

    answer = str(int(''.join(nums)))
    print(answer)

solution()
