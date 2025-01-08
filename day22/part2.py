"""
    I sort the bricks in ascending order of the smallest z coordinate,
then I drop them one by one onto the map.
    I store the map as a matrix of 10 x 10 tiles (seen from above), so
using the x and y axis. Each element of the matrix contains a height
and the id of the last brick that was dropped there. Initially, all the
elements are (0, None), so height 0, not belonging to any brick.
    Then I start dropping the bricks one by one. For each brick, I check
what is the highest point that will be covered by the brick (called the
peak). The brick will stand only on the points with the height equal to
this peak value. I add to a set the bricks that these points belong to,
these are the predecessors of the current brick. I also keep a set of
successors for each node, the current node being a successor for all its
predecessors.
    After dropping all the bricks, I have a complete set of predecessors
and successors for each brick.
    I then iterate again through the bricks and, for each brick, I count
the number of bricks that would fall if the current brick is disintegrated.
To do that, I start a BFS search from the current node and at each step, I
mark the current node as removed and continue exploring the successors only
as long as the all the predecessors of the successor were already removed.
A successor that has another predecessor that was not removed previously
will still stand on that predecessor, so it will not be taken into account.
I also update a counter that counts the number of nodes that will be removed
after the disintegration of the initial node.
"""
from collections import defaultdict, deque

INPUT_FILE = "input.txt"
MAX_X = 10
MAX_Y = 10

def solution(filename):
    def read_input():
        bricks = []
        with open(filename) as f:
            while line := f.readline().strip():
                end1, end2 = line.split("~")
                end1 = tuple(map(int, end1.split(",")))
                end2 = tuple(map(int, end2.split(",")))
                bricks.append((end1, end2))
        return bricks
    
    def solve():
        pred = defaultdict(set)
        succ = defaultdict(set)
        matrix = [[(0, None)] * MAX_X for _ in range(MAX_Y)]
        for n, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
            peak = max(matrix[i][j][0]
                       for i in range(x1, x2 + 1)
                       for j in range(y1, y2 + 1))
            height = peak + z2 - z1 + 1
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if matrix[i][j][0] == peak:
                        pred[n].add(matrix[i][j][1])
                        succ[matrix[i][j][1]].add(n)
                    matrix[i][j] = (height, n)
        return pred, succ
    
    def count_bfs(node):
        counter = 0
        queue = deque([node])
        removed = set()
        while queue:
            node = queue.popleft()
            removed.add(node)
            for node_succ in succ[node]:
                if len(pred[node_succ] - removed) == 0:
                    queue.append(node_succ)
                    counter += 1
        return counter
    
    bricks = read_input()
    bricks.sort(key=lambda x: x[0][2])
    pred, succ = solve()
    return sum(count_bfs(node) for node in range(len(bricks)))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
