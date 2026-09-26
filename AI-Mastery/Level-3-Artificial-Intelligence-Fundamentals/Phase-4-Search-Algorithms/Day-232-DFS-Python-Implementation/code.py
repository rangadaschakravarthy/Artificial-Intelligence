# Code — Day 232: DFS Python Implementation
from collections import deque
import heapq

# Sample Graph Representation
WEIGHTED_GRAPH = {
    'S': [('A', 2), ('B', 5)],
    'A': [('C', 2), ('D', 4)],
    'B': [('D', 1), ('G', 6)],
    'C': [('G', 3)],
    'D': [('G', 1)],
    'G': []
}

def breadth_first_search(graph, start, goal):
    queue = deque([(start, [start])])
    explored = set([start])
    
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        for neighbor, _ in graph.get(current, []):
            if neighbor not in explored:
                explored.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def uniform_cost_search(graph, start, goal):
    # Min-Heap stores (cost, current_node, path)
    pq = [(0, start, [start])]
    explored = set()
    
    while pq:
        cost, current, path = heapq.heappop(pq)
        if current == goal:
            return cost, path
        if current not in explored:
            explored.add(current)
            for neighbor, weight in graph.get(current, []):
                if neighbor not in explored:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return float('inf'), []

if __name__ == "__main__":
    print("Executing BFS Path Search...")
    bfs_path = breadth_first_search(WEIGHTED_GRAPH, 'S', 'G')
    print("BFS Path (Unweighted):", bfs_path)
    
    print("\nExecuting UCS Optimal Path Search...")
    ucs_cost, ucs_path = uniform_cost_search(WEIGHTED_GRAPH, 'S', 'G')
    print(f"UCS Optimal Cost: {ucs_cost}, Path: {ucs_path}")
