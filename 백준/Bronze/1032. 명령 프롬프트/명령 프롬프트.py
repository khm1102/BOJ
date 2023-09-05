N = int(input())

a = []
for i in range(N):
    a.append(input())

len_str = len(a[0])

if N == 1:
    print(a[0])
else:
    result = ''
    for i in range(len_str):
        check = True
        for j in range(1, N):
            if a[j][i] != a[0][i]:
                check = False
                break
        
        if check:
            result += a[0][i]
        else:
            result += '?'
    
    print(result)
