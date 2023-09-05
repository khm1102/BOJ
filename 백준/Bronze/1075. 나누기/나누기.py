N = int(input())
F = int(input())  

for i in range(0, 100):
    temp = N // 100 * 100 + i
    if temp % F == 0:
        print(str(i).zfill(2))  
        break
