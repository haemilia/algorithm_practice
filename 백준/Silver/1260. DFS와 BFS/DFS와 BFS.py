import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def dfs(graph, v, visited, n):
    visited[v] = True
    print(v, end=" ")
    for u in range(1, n+1):
        if (graph[v][u] == 1) and not visited[u]:
            dfs(graph, u, visited, n)

def bfs(graph, v, visited, n):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for u in range(1, n+1):
            if (graph[v][u] == 1) and not visited[u]:
                q.append(u)
                visited[u] = True
                
def main():
    n, m, v = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]


    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = graph[y][x] = 1

    visited = [False] * (n+1)
    dfs(graph, v, visited, n)
    print()
    visited = [False] * (n+1)
    bfs(graph, v, visited, n)

if __name__ == "__main__":
    main()