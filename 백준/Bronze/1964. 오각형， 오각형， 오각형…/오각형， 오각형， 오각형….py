n = int(input());k = 5;m = 7
for i in range(1, n):
    k += m
    m += 3
print(k % 45678)