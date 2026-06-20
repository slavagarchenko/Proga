from functools import reduce
from collections import deque


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def dfs(self, start, Visited=None):
        if Visited is None:
            Visited = set()
        Visited.add(start)
        result = [start]
        for neighbor in self.adjacency_list.get(start, []):
            if neighbor not in Visited:
                result.extend(self.dfs(neighbor, Visited))
        return result

    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            def add_neighbor(acc, neighbor):
                if neighbor not in visited:
                    visited.add(neighbor)
                    acc.append(neighbor)
                return acc

            queue.extend(
                reduce(add_neighbor, self.adjacency_list.get(vertex, []), []))

        return result

    def shortest_path(self, start, end, path=None, visited=None):
        if path is None:
            path = [start]
        if visited is None:
            visited = set([start])

        if start == end:
            return path

        shortest = None
        for neighbor in self.adjacency_list.get(start, []):
            if neighbor not in visited:
                new_path = self.shortest_path(
                    neighbor, end, path + [neighbor], visited | {neighbor})
                if new_path:
                    if shortest is None or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest

    def filter_vertices(self, predicate):
        return list(filter(predicate, self.adjacency_list.keys()))

    def __str__(self):
        return f"{self.adjacency_list}"


graph = Graph({
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
})

print(f"DFS из A: {graph.dfs('A')}")
print(f"BFS из A: {graph.bfs('A')}")
print(f"Кратчайший путь A -> F: {graph.shortest_path('A', 'F')}")
print(
    f"Вершины с соседями > 1: {graph.filter_vertices(lambda v: len(graph.adjacency_list[v]) > 1)}")
