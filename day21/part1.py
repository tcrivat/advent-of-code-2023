"""
    I keep a set of nodes (garden plots) that are currently
reachable on the map. For each step, I replace each node in
the set with the plots reachable from there in one step (its
neighbors). A neighbor is a one of the 4 nearby plots (in the
4 directions) that does not contain a rock.
    After 64 iterations, the set contains all the plots that
are reachable.
"""
INPUT_FILE = "input.txt"
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
STEPS = 64

def solution(filename):
    def read_input():
        matrix = []
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(line)
        return matrix
    
    def find_start():
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == "S":
                    return i, j
    
    def is_valid(node):
        return (0 <= node[0] < n and
                0 <= node[1] < n and
                matrix[node[0]][node[1]] != "#")
    
    def move(node, d):
        return (node[0] + d[0], node[1] + d[1])
    
    def get_neighbors(node):
        for d in DIRECTIONS:
            if is_valid(neigh := move(node, d)):
                yield neigh
    
    def solve_map(start):
        nodes = {start}
        for _ in range(STEPS):
            new_nodes = set()
            for node in nodes:
                new_nodes.update(get_neighbors(node))
            nodes = new_nodes
        return len(nodes)
    
    matrix = read_input()
    n = len(matrix)
    start = find_start()
    return solve_map(start)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
