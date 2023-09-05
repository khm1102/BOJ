def find_sequences(N, M, start, sequence):
    if M == 0:
        print(' '.join(map(str, sequence)))
        return

    for i in range(start, N + 1):
        find_sequences(N, M - 1, i, sequence + [i])

if __name__ == "__main__":
    N, M = map(int, input().split())
    find_sequences(N, M, 1, [])
