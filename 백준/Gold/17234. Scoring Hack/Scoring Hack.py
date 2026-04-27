from collections import deque

MAX = 1111
INF = 1e9

def input_values():
    N, A, B = map(int, input().split())
    return N, A, B

def checking(Score, Total_Turn, Double_Turn, N, A):
    return Score < N + A

def BFS(N, A, B):
    Visited = [[[False] * 11 for _ in range(MAX)] for _ in range(MAX)]
    Answer = INF

    Q = deque([(0, 0, 0)])
    Visited[0][0][0] = True

    while Q:
        NowT, NowX, NowD = Q.popleft()

        if NowX >= N:
            if checking(NowX, NowT, NowD, N, A):
                Answer = min(Answer, NowT)

        if not Visited[NowT + 1][NowX + A][NowD] and (NowX < N):
            Visited[NowT + 1][NowX + A][NowD] = True
            Q.append((NowT + 1, NowX + A, NowD))

        if not Visited[NowT + 1][NowX + B][NowD] and (NowX + B < N + A):
            Visited[NowT + 1][NowX + B][NowD] = True
            Q.append((NowT + 1, NowX + B, NowD))

        if not Visited[NowT + 1][NowX * 2][NowD + 1] and (NowX * 2 < N + A) and (NowD * 10 <= NowT - 9):
            Visited[NowT + 1][NowX * 2][NowD + 1] = True
            Q.append((NowT + 1, NowX * 2, NowD + 1))

    return Answer

def find_answer(Answer):
    print(Answer)

def main():
    N, A, B = input_values()
    Answer = BFS(N, A, B)
    find_answer(Answer)

if __name__ == "__main__":
    main()
