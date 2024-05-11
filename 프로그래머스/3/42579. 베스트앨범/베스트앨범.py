from collections import defaultdict

def solution(genres, plays):
    arr = defaultdict(list)
    res = []

    for i, (genres, plays) in enumerate(zip(genres, plays)):
        arr[genres].append((plays, i))

    rank = sorted(arr.keys(), key=lambda x: sum(play for play, _ in arr[x]), reverse=True)

    for i in rank:
        temp = sorted(arr[i], key=lambda x: (-x[0], x[1]))[:2]
        res.extend(idx for _, idx in temp)

    return res
