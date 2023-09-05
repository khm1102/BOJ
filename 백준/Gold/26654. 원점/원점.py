import math

def max_verts(N, A, B):
    a = math.sqrt(2 * A / (N * math.sin(2 * math.pi / N)))
    b = math.sqrt(B / math.pi)

    if a <= b:
        return N
    else:
        K = int(N * math.asin(b / a) / math.pi) + 1
        return K

T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    result = max_verts(N, A, B)
    print(result)