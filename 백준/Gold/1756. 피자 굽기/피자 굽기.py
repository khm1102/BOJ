def solve(D, N, oven, pizza_diameters):
    for i in range(1, D):
        oven[i] = min(oven[i], oven[i-1])
    
    depth = D 
    for pizza in pizza_diameters:
        while depth > 0 and oven[depth-1] < pizza:
            depth -= 1
        if depth == 0:
            return 0
        depth -= 1
    
    return depth + 1

D,N = map(int,input().split())
oven = list(map(int,input().split()))
pizza_diameters = list(map(int,input().split()))

print(solve(D, N, oven, pizza_diameters))
