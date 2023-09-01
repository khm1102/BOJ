def baseN(N, B):
    if N == 0:
        return "0"

    result = ""
    while N > 0:
        N, remainder = divmod(N, B)
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result

    return result

N, B = map(int, input().split())
print(baseN(N, B))
