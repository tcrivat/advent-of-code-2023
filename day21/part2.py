"""
    I use the following observations related to the structure of the
input map:
    - the start position is in the center of the map
    - both the line and the column that contain the starting position
do not have any rocks
    - there are also no rocks on the first or last column, or on the
first or last line
    As the map repeats infinitely, I think of the repeated maps as
tiles on a larger map. The original map corresponds to the (0, 0) tile,
the map repeated to the north to the (-1, 0) tile, to the east (0, 1)
etc.
    Because of the above-mentioned observations, the maps are reached
from the starting position in a very regular and ordered manner:
    - At first, only the map on the (0, 0) tile contains reachable plots.
    - After 66 (= n // 2 + 1) steps, the (-1, 0), (0, -1), (1, 0), (0, 1)
tiles (towards N, W, S, E) are reached. At step 66, all these 4 tiles
contain only one reachable plot in the middle of the line (or column)
closer to the (0, 0) tile. This is because it takes at least 66 steps
to reach that position from the center of the (0, 0) tile (= the starting
position), in a straight line from the starting position.
    - After 132 (= n + 1) steps, the (-1, -1), (1, -1), (-1, 1), (1, 1)
tiles (towards NW, SW, NE, SE) are reached. At step 132, all these 4
tiles contain only one reachable plot in the corner closer to the
(0, 0) tile. This is because it takes at least 132 steps to reach that
position from the starting position, in a straight line from the starting
position to the first/last line/column of the (0, 0) tile, then perpendicularly
towards the corner, along the edge.
    - After 197 = n + n // 2 + 1 steps, the process repeats and the
(-2, 0), (0, -2), (2, 0), (0, 2) tiles are reached, the first reached plot
being in the middle of the line (or column) closer to the (0, 0) tile.
    - At 263 = 2 * n + 1, the (-2, -1), (-2, 1), (-1, -2), (-1, 2),
(1, -2), (1, 2), (2, -1), (2, 1) tiles are reached, the first reachable
plot being in the corner towards the (0, 0) tile, and so on.
    So, in the end, there are 3 types of map tiles:
    - type 0: the (0, 0) tile where the exploration starts from the center
    - type 1: similar to tiles (-1, -1), (1, -1), (-1, 1), (1, 1) where
the exploration starts from a corner (4 different cases for each corner)
    - type 2: similar to tiles (-1, 0), (0, -1), (1, 0), (0, 1) where
the exploration starts from the center of an edge (first or last line or
column) - another 4 cases.
    In total we have 9 different kind of maps, all of the others are
identical to one of these 9 cases.
    To solve the problem, I precompute the number of plots reachable from
the starting position in each of these 9 cases. For each case, the number
of reachable plots steadily increases until the whole area of the map is
covered, and afterwards cycles between two values which are repeated to
infinity, as there are no new nodes which were not visited before on that
map. I stop iterating as soon as I detect that no new nodes are visited.
The values for a greater number of steps can be determined by taking the
last odd or even position (for an even number of steps I take the last
even position from this list), so there is no need to store more values.
    Now, for a given number of STEPS, the maximum tiles reached are at a
distance equal to (STEPS - 1) // n.
    To compute the result, for each distance from zero to the maximum, I
add the number of plots reachable from the tiles at that distance. For
example, for distance i, there are 4 * i tiles of type 1 (consisting of
i of each 4 cases in that type) and 4 tiles of type 2 (one for each 4 cases
of that type). For each such distance and each such map tile type, I compute
the step at which that tile was reached first and using the precomputed
number of plots, I add the corresponding value to the result.
    This solution requires the above-mentioned observations to be true,
which is not the case for the small exaple in the problem's statement. So
this does not work on the example.
"""
INPUT_FILE = "input.txt"
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
MAPS_BY_TYPE = {0: [(0, 0)],
                1: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
                2: [(-1, 0), (0, -1), (1, 0), (0, 1)]}
STEPS = 26501365

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
        for d in DIRECTIONS:
            if is_valid(neigh := move(node, d)):
                yield neigh
    
    def solve_map(start):
        counts = [0, 1]
        visited = {start}
        frontier = {start}
        while frontier:
            new_frontier = set()
            for node in frontier:
                for neigh in get_neighbors(node):
                    if neigh not in visited:
                        visited.add(neigh)
                        new_frontier.add(neigh)
            frontier = new_frontier
            counts.append(counts[-2] + len(frontier))
        return counts[1:-1]
    
    def precompute_counts():
        START = { -1: n - 1,
                   0: n // 2,
                   1: 0}
        counts_per_map = {}
        for i, j in sum(MAPS_BY_TYPE.values(), []):
            start = (START[i], START[j])
            counts_per_map[(i, j)] = solve_map(start)
        return counts_per_map
    
    def get_count(counts, step):
        if step < len(counts):
            return counts[step]
        elif step % 2 == len(counts) % 2:
            return counts[-2]
        else:
            return counts[-1]
    
    def solve():
        answer = get_count(counts_per_map[(0, 0)], STEPS)
        
        for i in range(0, (STEPS - 1) // n + 1):
            step = STEPS - i * n - 1
            for m in MAPS_BY_TYPE[1]:
                answer += i * get_count(counts_per_map[m], step)
            
            step -= n // 2
            if step < 0:
                break
            for m in MAPS_BY_TYPE[2]:
                answer += get_count(counts_per_map[m], step)
        return answer
    
    matrix = read_input()
    n = len(matrix)
    counts_per_map = precompute_counts()
    return solve()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
