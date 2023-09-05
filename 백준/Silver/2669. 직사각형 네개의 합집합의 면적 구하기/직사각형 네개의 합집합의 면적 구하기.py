board = [list(map(int, input().split())) for _ in range(4)]
check_cor = {(i, j) for rect in board for i in range(rect[0], rect[2]) for j in range(rect[1], rect[3])}
print(len(check_cor))
