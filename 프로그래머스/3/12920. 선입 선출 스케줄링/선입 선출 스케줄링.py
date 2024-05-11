def solution(n, cores):
    if n <= len(cores):
        return n

    n -= len(cores)

    left, right = 1, max(cores) * n

    while left < right:
        mid = (left + right) // 2
        done = sum(mid // core for core in cores)
        if done >= n:
            right = mid
        else:
            left = mid + 1
    done = sum((right - 1) // core for core in cores)
    n -= done
    for i, core in enumerate(cores, 1):
        if right % core == 0:
            n -= 1
            if n == 0:
                return i
