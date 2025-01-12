"""
    I visit the nodes in a topological order and for each
node I compute the longest path from start to that node as
the maximum of the longest path of its predecessors + 1.
Visiting the nodes in a topological order assures that all
the predecessors are already visited, so their longest path
is known.
    To visit the nodes in a topological order, I start with
a DFS-like search, however I stop the search whenever I
encounter a node with a predecessor which was not already
visited.
    To find the predecessors and successors of a node, I do
the following:
    - for a branching node (a node surrounded by <>^v), the
predecessors point towards the node, the successors point away
from the node
    - for all the other nodes, the predecessor is the neighbor
that was already visited, the successor is the neighbor that
is not visited yet
"""
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
                    neigh_symbol == "." and neigh not in distances):
                successors.append(neigh)
            else:
                predecessors.append(neigh)
        return predecessors, successors
    
    def visit(node):
        predecessors, successors = get_neighbors(node)
        if not all(pred in distances for pred in predecessors):
            return # will visit later
        distances[node] = 1 + max((distances[pred] for pred in predecessors),
                                  default=-1)
        for succ in successors:
            visit(succ)
    
    matrix = read_input()
    n = len(matrix)
    start = (0, 1)
    end = (n - 1, n - 2)
    distances = {}
    visit(start)
    return distances[end]

if __name__ == "__main__":
    print(solution(INPUT_FILE))
