def backtracking(N, M, arr, selected, depth):
    if depth == M:
        print(" ".join(map(str, selected)))
        return

    for i in range(len(arr)):
        if not selected or arr[i] >= selected[-1]:
            backtracking(N, M, arr, selected + [arr[i]], depth + 1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()  

    backtracking(N, M, numbers, [], 0)
