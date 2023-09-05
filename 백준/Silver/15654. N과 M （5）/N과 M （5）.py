def backtracking(nums, M, selected, sequence):
    if len(sequence) == M:  
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(len(nums)):
        if not selected[i]: 
            selected[i] = True
            sequence.append(nums[i])
            backtracking(nums, M, selected, sequence)
            selected[i] = False
            sequence.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))    
    numbers.sort()
    
    selected = [False] * N
    
    backtracking(numbers, M, selected, [])
