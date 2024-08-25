def solve(n, q, arr, op):
    shift = 0  

    for i in op:
        if i[0] == 1:
            i, x = i[1] - 1, i[2]
            arr[(i - shift) % n] += x
            
        elif i[0] == 2:
            s = i[1]
            shift = (shift + s) % n
            
        elif i[0] == 3:
            s = i[1]
            shift = (shift - s) % n

    return arr[-shift:] + arr[:-shift]

n, q = map(int, input().split())
print(" ".join(map(str, solve(n, q,list(map(int, input().split())),[list(map(int, input().split())) for _ in range(q)]))))
