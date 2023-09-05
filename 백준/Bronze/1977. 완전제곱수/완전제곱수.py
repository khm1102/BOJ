import math

M = int(input())
N = int(input())

min_value = int(1e9) 
sum_value = 0  

for i in range(M, N + 1):
    if math.sqrt(i) == int(math.sqrt(i)):
        min_value = min(min_value, i)  
        sum_value += i  

if sum_value == 0:  
    print(-1)
else:
    print(sum_value)
    print(min_value)
