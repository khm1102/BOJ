S = int(input())
N = int((2 * S) ** 0.5)  

while (N * (N + 1)) // 2 > S:N -= 1
print(N)  
