def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    
    remember_me = 0
    for i in range(start, n):
        if remember_me != nums[i]:
            temp.append(nums[i])
            remember_me = nums[i]
            dfs(i)
            temp.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    visited = [False] * n
    temp = []
    dfs(0)
