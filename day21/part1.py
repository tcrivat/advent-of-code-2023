"""
    I start exploring the map in a BFS-like manner, starting
from the position marked with "S". I keep a set of visited
nodes and another set of newly visited nodes (nodes visited
during the last iteration). Initially both sets contain the
start node.
    Then I do 64 iterations, one for each step, in which I
compute the new frontier (the new set of nodes that are
reachable for the first time during this iteration). The total
number of positions reachable after a number of steps is
equal to the number of steps reachable in the previous 2
iterations added with the number of new steps reachable during
the current iteration. This is true because for an area that
was already visited, the reachable positions alternate from one
iteration to the next: if a certain set of nodes are reachable
in one iteration, the others (positioned between them) will
become reachable during the next iteration, then again the same
set will become reachable again after yet another iteration/step.
    To compute the number of reachable positions after a certain
number of steps, only the last two values are needed (the number
of reachable positions after steps-1 and steps-2). So I only
keep in memory these last two values (c1 and c2).
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
        c1, c2 = 0, 1
        visited = {start}
        frontier = {start}
        for _ in range(STEPS):
            new_frontier = set()
            for node in frontier:
                for neigh in get_neighbors(node):
                    if neigh not in visited:
                        visited.add(neigh)
                        new_frontier.add(neigh)
            frontier = new_frontier
            c1, c2 = c2, c1 + len(frontier)
        return c2
    
    matrix = read_input()
    n = len(matrix)
    start = find_start()
    return solve_map(start)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
