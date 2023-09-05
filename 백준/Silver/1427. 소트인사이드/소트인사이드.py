n = int(input())
 
li = []
for i in str(n):
    li.append(int(i))

    
li.sort(reverse=True) 
 
for i in li:
    print(i,end='')