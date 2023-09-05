from collections import deque
def find(documents, target):
    queue = deque([(i, importance) for i, importance in enumerate(documents)])
    count = 0
    while queue:
        index, importance = queue.popleft()
        if any(importance < doc[1] for doc in queue):
            queue.append((index, importance))
        else:
            count += 1
            if index == target:
                return count
    return count
test_cases = int(input())
for _ in range(test_cases):
    n, m = map(int, input().split())
    documents = list(map(int, input().split()))
    print(find(documents, m))
