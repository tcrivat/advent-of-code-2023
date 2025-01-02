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
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    energized = set()
    trace((0, 0), RIGHT)
    return len(set(node for node, _ in energized))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
