def cmp(a, b):
    if a + b > b + a:
        return True
    return False

def largest_number(K, N, numbers):
    ans = []
    str_ = ""
    for i in range(K):
        tmp = numbers[i]
        if len(str_) < len(tmp) or (len(str_) == len(tmp) and str_ < tmp):
            str_ = tmp
        ans.append(tmp)

    for i in range(N - K):
        ans.append(str_)

    ans.sort(key=lambda x: x*10, reverse=True)

    return ''.join(ans)

K, N = map(int, input().split())
numbers = [input() for _ in range(K)]
result = largest_number(K, N, numbers)
print(result)
