def backtracking(N, M, length, selected, start):
    if length == M:
        print(' '.join(map(str, selected)))
        return
    
    for num in range(start, N + 1):
        if num not in selected:
            selected.append(num)
            backtracking(N, M, length + 1, selected, num + 1)
            selected.pop()

N, M = map(int, input().split())
backtracking(N, M, 0, [], 1)
