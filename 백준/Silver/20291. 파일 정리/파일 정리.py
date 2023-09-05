n = int(input())

file = dict()
for i in range(n):
    ex = (input().split('.'))[1]
    
    if not ex in file:file[ex] = 1
    
    else:file[ex] += 1

sort_file = sorted(file.items())

for key, value in sort_file: print(key, value)
