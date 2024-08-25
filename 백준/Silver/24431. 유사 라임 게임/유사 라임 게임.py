def solve(n, l, f, w):
    suffix_dict = {}

    for i in w:
        suffix = i[-f:]  
        
        if suffix in suffix_dict:
            suffix_dict[suffix].append(i)
            
        else:
            suffix_dict[suffix] = [i]

    temp = 0
    for i in suffix_dict.values():
        temp += len(i) // 2
    
    return temp

for _ in range(int(input())):
    n, l, f = map(int, input().split())
    print(solve(n,l,f,input().split()))
