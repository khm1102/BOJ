def solution():
    a, b = map(int, input().split())
    
    if a + b == 0:
        print("125.00 125.00")
        return
    
    base = 250.0 * 250.0 / 2
    
    if a > 0 and b > 0:
        print(f"0.00 {250.0 - base / max(a, b):.2f}" if a > b else f"{250.0 - base / max(a, b):.2f} 0.00")
        return

    if a < 125 and b == 0:
        tmp = 250.0 - base / (250 - a)
        print(f"{tmp:.2f} {250.0 - tmp:.2f}")
        return

    if a == 0 and b < 125:
        tmp = 250.0 - base / (250 - b)
        print(f"{250.0 - tmp:.2f} {tmp:.2f}")
        return

    if b == 0:
        print(f"0.00 {base / a:.2f}")
        return

    print(f"{base / b:.2f} 0.00")

if __name__ == "__main__":
    solution()
