print("correct!" if (lambda x: x[0] + x[1] == x[2])(list(map(int, input().split()))) else "wrong!")
