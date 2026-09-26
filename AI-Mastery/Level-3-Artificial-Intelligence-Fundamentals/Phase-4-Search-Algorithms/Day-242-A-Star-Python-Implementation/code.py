# Code — Day 242: A* Python Implementation
import heapq

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_grid_solver(grid, start, goal):
    """A* Pathfinding on a 2D Grid (0 = empty, 1 = wall)."""
    rows, cols = len(grid), len(grid[0])
    open_set = []
    # (f_score, g_score, current_node, path)
    heapq.heappush(open_set, (manhattan_distance(start, goal), 0, start, [start]))
    
    g_scores = {start: 0}
    closed_set = set()
    nodes_expanded = 0
    
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        
        if current in closed_set:
            continue
        closed_set.add(current)
        nodes_expanded += 1
        
        if current == goal:
            return path, g, nodes_expanded
            
        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor in closed_set:
                    continue
                tentative_g = g + 1
                if tentative_g < g_scores.get(neighbor, float('inf')):
                    g_scores[neighbor] = tentative_g
                    f_score = tentative_g + manhattan_distance(neighbor, goal)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor, path + [neighbor]))
                    
    return None, float('inf'), nodes_expanded

if __name__ == "__main__":
    # Sample 5x5 Maze: 0 = Open, 1 = Wall
    maze = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_pos = (0, 0)
    goal_pos = (4, 4)
    
    print(f"Executing A* Pathfinding from {start_pos} to {goal_pos}...")
    path, cost, expanded = a_star_grid_solver(maze, start_pos, goal_pos)
    print(f"Optimal Path Found ({len(path)} steps): {path}")
    print(f"Total Path Cost g(n): {cost}")
    print(f"Total Nodes Expanded: {expanded}")
