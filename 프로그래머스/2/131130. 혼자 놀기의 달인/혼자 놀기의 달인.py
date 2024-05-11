def solution(cards):
    def find_group(start, visited, cards):
        next_card = cards[start - 1]
        if visited[next_card]:
            return 0
        visited[next_card] = True
        return 1 + find_group(next_card, visited, cards)
    
    scores = []
    visited = [False] * (len(cards) + 1)
    for i in range(1, len(cards) + 1):
        if not visited[i]:
            scores.append(find_group(i, visited, cards))
    
    scores.sort(reverse=True)
    return scores[0] * scores[1] if len(scores) > 1 else 0