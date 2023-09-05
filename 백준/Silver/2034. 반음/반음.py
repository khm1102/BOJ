n = int(input())
arr = [0] * 10001
piano = ['C', 'X', 'D', 'X', 'E', 'F', 'X', 'G', 'X', 'A', 'X', 'B']

for i in range(n):
    arr[i] = int(input())
    arr[i] %= 12

for c in 'ABCDEFG':
    idx = 0
    last = ''
    
    for i in range(12):
        if piano[i] == c:
            idx = i
            break
    
    chk = True
    for i in range(n):
        idx += arr[i]
        idx %= 12
        if idx < 0:
            idx += 12
        
        if piano[idx] == 'X':
            chk = False
            break
        last = piano[idx]
    
    if chk:
        print(c, last)
