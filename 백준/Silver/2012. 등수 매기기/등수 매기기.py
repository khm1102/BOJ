def min_discontentment(N, expected_ranks):
    sorted_ranks = sorted(expected_ranks)
    discontentment = 0
    
    for i in range(N):
        discontentment += abs(sorted_ranks[i] - (i + 1))
    
    return discontentment

if __name__ == "__main__":
    N = int(input())
    expected_ranks = []
    for _ in range(N):
        expected_ranks.append(int(input()))
    
    result = min_discontentment(N, expected_ranks)
    print(result)
