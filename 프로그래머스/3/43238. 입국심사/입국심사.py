def solution(n, times):
    
    left, right = 1, max(times) *n
    answer = right
    
    
    while (left <= right):
        
        mid = (left + right) // 2
        res = sum(mid // i for i in times)
        
        if res >= n:
            answer = min(answer, mid)
            right = mid - 1
        
        else: 
            left = mid + 1
    
    return answer