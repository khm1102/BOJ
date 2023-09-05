def get_decomposition_sum(num):
    return sum(map(int, str(num)))

def find_generator(n):
    for i in range(1, n+1):
        if i + get_decomposition_sum(i) == n:
            return i
    return 0

n = int(input())

result = find_generator(n)

print(result)
