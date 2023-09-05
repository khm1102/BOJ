n = int(input())
Arraylist = []

for i in range(n):
    Arraylist.append(int(input()))
Arraylist.sort()
print(round(sum(Arraylist)/len(Arraylist)))
print(Arraylist[len(Arraylist)//2])


dic = dict()

for i in Arraylist:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_dic =[]

for i in dic:
    if dic[i] == mx:
        mx_dic.append(i)

if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])


print(max(Arraylist)-min(Arraylist))
