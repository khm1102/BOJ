
class Main:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.edge = [[] for _ in range(N + 1)]
        self.matched = [0] * (N + 1)
        self.visit = [False] * (N + 1)

    def add_edge(self, a, b):
        self.edge[a].append(b)

    def DFS(self, vertex):
        for want_vertex in self.edge[vertex]:
            if self.visit[want_vertex]:
                continue
            self.visit[want_vertex] = True
            if self.matched[want_vertex] == 0:
                self.matched[want_vertex] = vertex
                return True
            else:
                move_vertex = self.matched[want_vertex]
                if self.DFS(move_vertex):
                    self.matched[want_vertex] = vertex
                    return True
        return False

    def init_visit(self):
        self.visit = [False] * (self.N + 1)

    def solution(self):
        answer = 0
        for i in range(1, self.N + 1):
            self.init_visit()
            if self.DFS(i):
                answer += 1
        return answer

def main():
    n, m = map(int, input().split())
    graph = Main(n, m)

    for _ in range(m):
        a, b = map(int, input().split())
        graph.add_edge(a, b)

    print(graph.solution())

if __name__ == "__main__":
    main()
