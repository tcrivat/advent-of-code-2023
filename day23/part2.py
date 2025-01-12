"""
    I construct a new undirected weighted graph that contains
only the branching nodes (nodes surrounded by <>^v) from the
original graph, with weights equal to the number of steps
between them. To construct this graph, I visit the nodes in
the original graph in the same topological order as in part 1.
    On this undirected weighted graph I run a backtracking
algorithm to explore all the possible paths between START and
END, storing the length of the longest path encountered in a
variable.
"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

INPUT_FILE = "input.txt"
DIRECTIONS = {(-1,  0): "^",
              ( 0, -1): "<",
              ( 0,  1): ">",
              ( 1,  0): "v"}

def solution(filename):
    def read_input():
        matrix = []
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(line)
        return matrix
    
    def is_valid(node):
        return (0 <= node[0] < n and
                0 <= node[1] < n and
                matrix[node[0]][node[1]] != "#")
    
    def move(node, d):
        return (node[0] + d[0], node[1] + d[1])
    
    def get_neighbors(node):
        predecessors = []
        successors = []
        for d in DIRECTIONS:
            neigh = move(node, d)
            if not is_valid(neigh):
                continue
            neigh_symbol = matrix[neigh[0]][neigh[1]]
            if (neigh_symbol == DIRECTIONS[d] or
                    neigh_symbol == "." and neigh not in visited):
                successors.append(neigh)
            else:
                predecessors.append(neigh)
        return predecessors, successors
    
    def visit(prev, node, dist):
        predecessors, successors = get_neighbors(node)
        if len(predecessors) > 1 or len(successors) > 1 or node == end:
            adj[prev].append((node, dist))
            adj[node].append((prev, dist))
            prev = node
            dist = 0
        if not all(pred in visited for pred in predecessors):
            return # will visit later
        visited.add(node)
        for succ in successors:
            visit(prev, succ, dist + 1)
    
    def solve(node, dist):
        if node == end:
            nonlocal max_length
            max_length = max(dist, max_length)
            return
        visited.add(node)
        for neigh, weight in adj[node]:
            if neigh not in visited:
                solve(neigh, dist + weight)
        visited.remove(node)
    
    matrix = read_input()
    n = len(matrix)
    start = (0, 1)
    end = (n - 1, n - 2)
    
    visited = set()
    adj = defaultdict(list)
    visit(start, start, 0)
    
    visited.clear()
    max_length = 0
    solve(start, 0)
    return max_length

if __name__ == "__main__":
    print(solution(INPUT_FILE))
