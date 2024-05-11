def solution(pgs, sps):
    dl = [(100 - p) // s if (100 - p) % s == 0 else (100 - p) // s + 1 for p, s in zip(pgs, sps)]
    ans = []
    cur_max = dl[0]
    
    ft = 1
    for day in dl[1:]:
        if day <= cur_max: 
            ft += 1
        else:
            ans.append(ft)
            ft = 1 
            cur_max = day
    ans.append(ft)
    
    return ans
