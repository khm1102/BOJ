def is_valid(N, L, W, H, A):
    return (L // A) * (W // A) * (H // A) >= N

def find_max_A(N, L, W, H):
    low = 0.0
    high = 1000000001.0
    for _ in range(1000):
        mid = (low + high) / 2
        if is_valid(N, L, W, H, mid):
            low = mid
        else:
            high = mid
    return low


N, L, W, H = map(int, input().split())

print(f"{find_max_A(N, L, W, H):.9f}")