import heapq

def prims(graph, start):
    visited = set()
    min_heap = [(0, start)]
    mst_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst_cost += cost
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

    print("Minimum Cost of MST:", mst_cost)

# -------- User Input Section --------
graph = {}
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

print("Enter edges in format: node1 node2 weight")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))  # because the graph is undirected

start_node = input("Enter starting node: ")
prims(graph, start_node)
