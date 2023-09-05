n = int(input())
lst = []

for i in range(n):
    lst.append(input())
set_lst = set(lst)	
lst = list(set_lst)	
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)