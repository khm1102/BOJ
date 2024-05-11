from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    arr = set()
    for i in range(1, len(numbers) + 1):
        perm = permutations(numbers, i)
        for p in perm:
            num = int(''.join(p))
            
            if num not in arr:
                arr.add(num)
                if is_prime(num):
                    answer += 1
    return answer