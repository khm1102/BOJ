import sys

sys.setrecursionlimit(10 ** 6)


def find_root(lnks, n):
    parent = [-1] * n
    for i in range(n):
        lft, rgt = lnks[i]
        if lft != -1:
            parent[lft] = i
        if rgt != -1:
            parent[rgt] = i
    return next(i for i, p in enumerate(parent) if p == -1)


def dfs(root, nums, lnks, max_grp_sum):
    stack = [(root, 0)]
    sums = {}
    grp_cnt = [0]

    while stack:
        node, state = stack.pop()
        if node == -1:
            continue

        if state == 0:
            stack.append((node, 1))
            stack.append((lnks[node][0], 0))
            stack.append((lnks[node][1], 0))
        else:
            lft_sum = sums.get(lnks[node][0], 0)
            rgt_sum = sums.get(lnks[node][1], 0)
            cur_sum = nums[node]

            if cur_sum + lft_sum + rgt_sum <= max_grp_sum:
                sums[node] = cur_sum + lft_sum + rgt_sum
            elif cur_sum + min(lft_sum, rgt_sum) <= max_grp_sum:
                grp_cnt[0] += 1
                sums[node] = cur_sum + min(lft_sum, rgt_sum)
            else:
                grp_cnt[0] += 2
                sums[node] = cur_sum

    return sums[root], grp_cnt[0] + 1


def part(root, nums, lnks, max_grp_sum, k):
    _, grp_cnt = dfs(root, nums, lnks, max_grp_sum)
    return grp_cnt <= k


def solution(k, nums, lnks):
    n = len(nums)
    root = find_root(lnks, n)

    l, r = max(nums), sum(nums)
    ans = r

    while l <= r:
        mid = (l + r) // 2
        if part(root, nums, lnks, mid, k):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans
