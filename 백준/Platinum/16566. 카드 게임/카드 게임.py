import sys
import bisect

def main():
    input = sys.stdin.readline
    _, m, k = map(int, input().split())
    cards = sorted(map(int, input().split()))
    magician = map(int, input().split())
    parent = list(range(m + 1))

    for card in magician:
        idx = bisect.bisect_right(cards, card)
        while parent[idx] != idx:
            idx = parent[idx]
        print(cards[idx])
        if idx < m:
            parent[idx] = idx + 1

if __name__ == "__main__":
    main()
