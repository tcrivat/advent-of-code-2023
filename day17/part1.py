"""
    The solution uses Dijkstra's algorithm to compute the shortest
path between the START and END tiles. To take into account the limit
on the number of consecutive steps that can be taken in the same
direction, a node in the graph stores the coordinates of the tile,
the direction from which the tile was reached and the number of
consecutive steps that were taken in this direction before reaching
the tile.
    To find the neighbors of a certain node, I look at the tile in front
(same direction) only if the maximum number of steps was not reached.
The tiles to the right or left are always neighbors, as turning (left
or right) resets the steps count.
    The algorithm finishes when the end tile is reached.
"""
from heapq import heapify, heappop, heappush

INPUT_FILE = "input.txt"
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
MAX_STEPS = 3

def solution(filename):
    def read_input():
        matrix = []
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(list(map(int, line)))
        return matrix
    
    def turn(dir):
        if dir[0]:
            return [(0, -1), (0, 1)]
        else:
            return [(-1, 0), (1, 0)]
    
    def move(coord, dir, steps):
        coord = coord[0] + dir[0], coord[1] + dir[1]
        if 0 <= coord[0] < n and 0 <= coord[1] < m:
            yield coord, dir, steps
    
    def get_neighbors(node):
        coord, dir, steps = node
        if steps < MAX_STEPS: # move forward
            yield from move(coord, dir, steps + 1)
        for new_dir in turn(dir): # move right or left
            yield from move(coord, new_dir, 1)
    
    def solve_dijkstra(start, start_dir):
        priority_queue = [] # items: (distance, (coordinates, direction, steps))
        heapify(priority_queue)
        for dir in start_dir:
            node = (start, dir, 0)
            distances[node] = 0
            heappush(priority_queue, (0, node))
        
        while priority_queue:
            dist, node = heappop(priority_queue)
            for neigh in get_neighbors(node):
                neigh_coord = neigh[0]
                neigh_dist = dist + matrix[neigh_coord[0]][neigh_coord[1]]
                if (neigh_dist < distances.get(neigh, neigh_dist + 1)):
                    prev[neigh] = node
                    distances[neigh] = neigh_dist
                    if neigh_coord == end:
                        return neigh_dist, neigh
                    heappush(priority_queue, (neigh_dist, neigh))
    
    def print_map():
        for i in range(n):
            for j in range(m):
                print(matrix[i][j], end="")
            print()
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    
    distances = {}
    prev = {}
    start = (0, 0)
    start_dir = [(0, 1), (1, 0)]
    end = (n - 1, m - 1)
    min_distance, node = solve_dijkstra(start, start_dir)
    
    # ~ while node:
        # ~ coord = node[0]
        # ~ matrix[coord[0]][coord[1]] = " "
        # ~ node = prev.get(node, None)
    # ~ print_map()
    
    return min_distance

if __name__ == "__main__":
    print(solution(INPUT_FILE))
