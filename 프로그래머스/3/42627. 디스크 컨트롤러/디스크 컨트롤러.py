import heapq

def solution(jobs):
    ans, end, index, cnt = 0, 0, 0, 0
    jobs.sort(key=lambda x: x[0])
    pq = []

    while cnt < len(jobs):
        while index < len(jobs) and jobs[index][0] <= end:
            heapq.heappush(pq, (jobs[index][1], jobs[index][0]))
            index += 1

        if not pq:
            end = jobs[index][0]

        else:
            temp = heapq.heappop(pq)
            ans += temp[0] + end - temp[1]
            end += temp[0]
            cnt += 1

    return int(ans / len(jobs))
