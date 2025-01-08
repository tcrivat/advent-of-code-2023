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
this peak value. I check to which bricks these points belong (the
predecessors of the current brick). If there is only one predecessor,
then that predecessor is not safe to remove, as it will cause the current
brick to collapse. I mark it as such.
    After dropping all the bricks, the answer is the total number of bricks
minus the number of bricks marked as not safe.
"""
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
        not_safe = set()
        matrix = [[(0, None)] * MAX_X for _ in range(MAX_Y)]
        for n, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
            peak = max(matrix[i][j][0]
                       for i in range(x1, x2 + 1)
                       for j in range(y1, y2 + 1))
            height = peak + z2 - z1 + 1
            pred = set()
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if matrix[i][j][0] == peak:
                        pred.add(matrix[i][j][1])
                    matrix[i][j] = (height, n)
            if len(pred) == 1:
                pred.discard(None)
                not_safe.update(pred)
        return len(bricks) - len(not_safe)
    
    bricks = read_input()
    bricks.sort(key=lambda x: x[0][2])
    return solve()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
