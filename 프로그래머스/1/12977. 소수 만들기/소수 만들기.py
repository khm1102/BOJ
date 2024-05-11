def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    from itertools import combinations

    answer = 0
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            answer += 1
    return answer
