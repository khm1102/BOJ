n = int(input())
nums = list(map(int, input().split(' '))) 
resCnt = 0 

for i in nums:
    cnt = 0 
    if(i == 1): 
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        resCnt += 1
print(resCnt)