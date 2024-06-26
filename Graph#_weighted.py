from collections import deque

class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt

def create_graph(graph):
    for i in range(len(graph)):
        graph[i] = []
    graph[0].append(Edge(0, 1, 1))
    graph[0].append(Edge(0, 2, 1))
    graph[1].append(Edge(1, 0, 1))
    graph[1].append(Edge(1, 3, 1))
    graph[2].append(Edge(2, 0, 1))
    graph[2].append(Edge(2, 4, 1))
    graph[3].append(Edge(3, 1, 1))
    graph[3].append(Edge(3, 4, 1))
    graph[3].append(Edge(3, 5, 1))
    graph[4].append(Edge(4, 2, 1))
    graph[4].append(Edge(4, 3, 1))
    graph[4].append(Edge(4, 5, 1))
    graph[5].append(Edge(5, 3, 1))
    graph[5].append(Edge(5, 4, 1))
    graph[5].append(Edge(5, 6, 1))
    graph[6].append(Edge(6, 5, 1))

def bfs(graph, V):
    visited = [False] * V
    q = deque([0])  # Source = 0
    while q:
        curr = q.popleft()
        if not visited[curr]:
            print(curr, end=" ")
            visited[curr] = True
            for e in graph[curr]:
                q.append(e.dest)
    print()

if __name__ == "__main__":
    """
    1 --- 3
    / | \
    0 | 5 -- 6
    \ | /
    2 ---- 4
    """
    V = 7
    graph = [[] for _ in range(V)]
    create_graph(graph)
    bfs(graph, V)
