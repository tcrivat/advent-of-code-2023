"""
    I do two passes through the loop: the first one to mark
the track, the second one to identify the right and left sides
of the track. For each identified neighbor on the right or left
sides, I fill the map recursively with the appropriate marking
("L" or "R") until I reach the track or the edge of the map. If
I reach the edge of the map, I flag the specified marking as
being outside of the loop (the inside can never reach the edge
of the map).
"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

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

RIGHT = {("|", N): [E],
         ("|", S): [W],
         ("-", E): [S],
         ("-", W): [N],
         ("L", N): [],
         ("L", E): [W, S],
         ("J", N): [S, E],
         ("J", W): [],
         ("7", S): [],
         ("7", W): [E, N],
         ("F", S): [N, W],
         ("F", E): [],
         ("S", N): [E],
         ("S", S): [W],
         ("S", E): [S],
         ("S", W): [N]}

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
    
    def get_neighbors(node, marking):
        for d in DIRECTIONS[matrix[node[0]][node[1]]]:
            neigh = move(node, d)
            if (0 <= neigh[0] < n and # on map
                    0 <= neigh[1] < m and
                    markings[neigh] == marking and
                    (-1 * d[0], -1 * d[1]) in # pipes are connected
                        DIRECTIONS[matrix[neigh[0]][neigh[1]]]):
                yield neigh, d
    
    def mark_track(node):
        while node:
            markings[node] = "1"
            node, _ = next(get_neighbors(node, ""), (None, None))
    
    def fill(node, symbol):
        if not (0 <= node[0] < n and
                    0 <= node[1] < m):
            return False # not on map is outside
        
        if node in markings:
            return True # already marked
        
        markings[node] = symbol
        return all([fill(move(node, d), symbol)]
                    for d in (N, S, E, W))
    
    def mark_left_right(node):
        inside = None
        while node:
            markings[node] = "2"
            next_node, dir = next(get_neighbors(node, "1"), (None, None))
            
            if next_node:
                symbol = matrix[node[0]][node[1]]
                right_side = [move(node, d)
                              for d in RIGHT[(symbol, dir)]]
                for node_right in right_side:
                    if not fill(node_right, "R"):
                        inside = "L"
                
                left_side = [move(node, d)
                             for d in (N, S, E, W)
                             if d not in RIGHT[(symbol, dir)]]
                for node_left in left_side:
                    if not fill(node_left, "L"):
                        inside = "R"
                
            node = next_node
        return inside
    
    def count_nodes(inside):
        return sum(markings[(i, j)] == inside
                   for i in range(n)
                   for j in range(m))
    
    def print_map():
        for i in range(n):
            for j in range(m):
                print(markings[(i, j)], end="")
            print()
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    start = find_node("S")
    markings = defaultdict(str)
    mark_track(start)
    inside = mark_left_right(start)
    # ~ print_map()
    # ~ print("inside:", inside)
    return count_nodes(inside)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
