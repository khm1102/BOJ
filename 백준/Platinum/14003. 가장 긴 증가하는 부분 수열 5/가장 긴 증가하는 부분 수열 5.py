def solution():
    global N, Arr, Index_Arr, V
    for i in range(1, N + 1):
        if len(V) == 0 or V[-1] < Arr[i]:
            V.append(Arr[i])
            Index_Arr[i] = len(V) - 1
        else:
            Left = 0
            Right = len(V) - 1
            while Left < Right:
                Mid = (Left + Right) // 2
                if V[Mid] >= Arr[i]:
                    Right = Mid
                else:
                    Left = Mid + 1
            V[Left] = Arr[i]
            Index_Arr[i] = Left

    print(len(V))
    Answer = []
    Find_Index = len(V) - 1
    for i in range(N, 0, -1):
        if Index_Arr[i] == Find_Index:
            Find_Index -= 1
            Answer.append(Arr[i])

    for i in range(len(Answer) - 1, -1, -1):
        print(Answer[i], end=" ")

def solve():
    global N, Arr, Index_Arr, V
    N = int(input())
    Arr = [0] + list(map(int, input().split()))
    Index_Arr = [0] * (N + 1)
    V = []

    solution()

if __name__ == "__main__":
    solve()
