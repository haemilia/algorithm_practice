import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

num_cities = int(input())
num_buses = int(input())
graph = [[] for _ in range(num_cities + 1)]
for _ in range(num_buses):
    fr, to, fare = map(int, input().split())
    graph[fr].append((to, fare))

def dijkstra_heap(graph, start):
    distances = [INF] * (num_cities + 1)
    distances[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distances

dep, dest = map(int, input().split())
distances = dijkstra_heap(graph, dep)
print(distances[dest])