import heapq
class StackItem:
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state

N = int(input())
vec = []
for _ in range(N):
    x, r = map(int, input().split())
    vec.append((x - r, -1))
    vec.append((x + r, 1))

vec.sort(key=lambda x: (x[0], -x[1]))

ans = 0
last = 0
st = []

for i in range(len(vec)):
    if not st:
        st.append(StackItem(vec[i][0], 0))
        last = vec[i][0]
    elif vec[i][1] == -1:
        if vec[i][0] == last:
            vec_tmp = []
            tmp = st.pop()
            if tmp.state != -1:
                tmp.state = 1
            st.append(tmp)
            st.append(StackItem(vec[i][0], 0))
        else:
            tmp = st.pop()
            tmp.state = -1
            st.append(tmp)
            st.append(StackItem(vec[i][0], 0))
            last = vec[i][0]
    elif vec[i][1] == 1:
        tmp = st.pop()
        if tmp.state == 1 and last == vec[i][0]:
            ans += 2
        else:
            ans += 1
        last = vec[i][0]

print(ans + 1)
