"""
"""
import sys
sys.setrecursionlimit(10000)

INPUT_FILE = "input.txt"

UP    = (-1,  0)
DOWN  = ( 1,  0)
RIGHT = ( 0,  1)
LEFT  = ( 0, -1)

REFLECT = {("/" , RIGHT): [UP],
           ("/" , LEFT ): [DOWN],
           ("/" , UP   ): [RIGHT],
           ("/" , DOWN ): [LEFT],
           ("\\", RIGHT): [DOWN],
           ("\\", LEFT ): [UP],
           ("\\", UP   ): [LEFT],
           ("\\", DOWN ): [RIGHT],
           ("|" , RIGHT): [UP, DOWN],
           ("|" , LEFT ): [UP, DOWN],
           ("-" , UP   ): [LEFT, RIGHT],
           ("-" , DOWN ): [LEFT, RIGHT]}

def solution(filename):
    def read_input():
        matrix = []
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(line)
        return matrix
    
    def move(node, d):
        return node[0] + d[0], node[1] + d[1]
    
    def trace(node, d):
        if not (0 <= node[0] < n and
                0 <= node[1] < m and
                (node, d) not in energized):
            return
        energized.add((node, d))
        symbol = matrix[node[0]][node[1]]
        if (symbol, d) in REFLECT:
            for new_d in REFLECT[(symbol, d)]:
                trace(move(node, new_d), new_d)
        else:
            trace(move(node, d), d)
    
    def solve():
        start = []
        for i in range(n):
            start.append(((i, 0), RIGHT))
            start.append(((i, m - 1), LEFT))
        for j in range(m):
            start.append(((0, j), DOWN))
            start.append(((n - 1, j), UP))
        max_energized = 0
        for node, d in start:
            energized.clear()
            trace(node, d)
            current = len(set(node for node, _ in energized))
            max_energized = max(max_energized, current)
        return max_energized
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    energized = set()
    return solve()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
