"""
    A pipe on a neighboring node is connected if it has an entrance
in the opposite direction than the current pipe (N connects with S,
W connects with E).
    I use BFS to count the steps from the start to the other side of
the loop. The last node visited is the one furthest from the start.
"""
from collections import deque

INPUT_FILE = "input.txt"

N = (-1,  0)
S = ( 1,  0)
E = ( 0,  1)
W = ( 0, -1)

DIRECTIONS = {"|": [N, S],
              "-": [E, W],
              "L": [N, E],
              "J": [N, W],
              "7": [S, W],
              "F": [S, E],
              ".": [],
              "S": [N, S, E, W]}

def solution(filename):
    def read_input():
        matrix = []
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(line)
        return matrix
    
    def find_node(symbol):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == symbol:
                    return i, j
    
    def move(node, d):
        return node[0] + d[0], node[1] + d[1]
    
    def get_neighbors(node):
        for d in DIRECTIONS[matrix[node[0]][node[1]]]:
            neigh = move(node, d)
            if (0 <= neigh[0] < n and # on map
                    0 <= neigh[1] < m and
                    (-1 * d[0], -1 * d[1]) in # pipes are connected
                        DIRECTIONS[matrix[neigh[0]][neigh[1]]]):
                yield neigh
    
    def solve_bfs(start):
        dist = {start: 0}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neigh in get_neighbors(node):
                if neigh not in dist: # not visited
                    dist[neigh] = dist[node] + 1
                    queue.append(neigh)
        return dist[node]
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    start = find_node("S")
    return solve_bfs(start)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
