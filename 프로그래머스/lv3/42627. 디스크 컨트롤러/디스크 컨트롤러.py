import heapq

def solution(jobs):
    answer = 0
    end = 0  
    jobsIdx = 0 
    count = 0 

    jobs.sort(key=lambda x: x[0])

    pq = []

    while count < len(jobs):

        while jobsIdx < len(jobs) and jobs[jobsIdx][0] <= end:
            heapq.heappush(pq, (jobs[jobsIdx][1], jobs[jobsIdx][0]))
            jobsIdx += 1

        if not pq:
            end = jobs[jobsIdx][0]

        else:
            temp = heapq.heappop(pq)
            answer += temp[0] + end - temp[1]
            end += temp[0]
            count += 1

    return int(answer / len(jobs))
