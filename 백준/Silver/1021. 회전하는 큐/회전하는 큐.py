from collections import deque


N, M = map(int, input().split())
queue = deque(range(1, N + 1))

positions = list(map(int, input().split()))

moves = 0  

for p in positions:
    left_moves = queue.index(p)
    right_moves = len(queue) - left_moves
    min_moves = min(left_moves, right_moves)
    if min_moves == left_moves:
        queue.rotate(-left_moves)  
    else:
        queue.rotate(right_moves)  

    queue.popleft()
    moves += min_moves

print(moves)
