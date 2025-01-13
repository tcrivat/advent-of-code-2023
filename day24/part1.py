"""
    For two hailstones' trajectories to intersect, they must both
pass through the same spot at some point in time.
    For the hailstones with the following positions and velocities:
        p1[X] p1[Y] p1[Z] @ v1[X] v1[Y] v1[Z]
                        and
        p2[X] p2[Y] p2[Z] @ v2[X] v2[Y] v2[Z]
let's say their trajectories will cross at the point (x, y) at
times t1 for the first and t2 for the second hailstone. Note that
t1 does not have to be equal with t2, only the trajectories need to
cross, not the hailstones themselves.
    Then:
        x = p1[X] + v1[X] * t1
        y = p1[Y] + v1[Y] * t1
                 and
        x = p2[X] + v2[X] * t2
        y = p2[Y] + v2[Y] * t2
    This means that:
         p1[X] + v1[X] * t1 = p2[X] + v2[X] * t2
         p1[Y] + v1[Y] * t1 = p2[Y] + v2[Y] * t2
    Solving for t1 and t2 results in:
        t1 = ((v2[X] * (p1[Y] - p2[Y]) - v2[Y] * (p1[X] - p2[X])) /
              (v1[X] * v2[Y] - v1[Y] * v2[X]))
        t2 = (p1[X] - p2[X] + v1[X] * t1) / v2[X]
    So, for the trajectories to cross:
        v1[X] * v2[Y] != v1[Y] * v2[X]
    Also t1 and t2 should not be in the past (t1 > 0 and t2 > 0).
    And, of course, x and y should be inside the designated area.
"""
INPUT_FILE = "input.txt"
AREA_MIN = 200000000000000
AREA_MAX = 400000000000000
X = 0
Y = 1

def solution(filename):
    def read_input():
        hailstones = []
        with open(filename) as f:
            while line := f.readline().strip():
                position, velocity = line.split(" @ ")
                position = tuple(map(int, position.split(", ")))
                velocity = tuple(map(int, velocity.split(", ")))
                hailstones.append((position, velocity))
        return hailstones
    
    def solve():
        answer = 0
        for i in range(len(hailstones)):
            p1, v1 = hailstones[i]
            for j in range(i):
                p2, v2 = hailstones[j]
                if (v1[X] * v2[Y] != v1[Y] * v2[X]):
                    t1 = ((v2[X] * (p1[Y] - p2[Y]) - v2[Y] * (p1[X] - p2[X])) /
                          (v1[X] * v2[Y] - v1[Y] * v2[X]))
                    if t1 <= 0:
                        continue
                    t2 = (p1[X] - p2[X] + v1[X] * t1) / v2[X]
                    if t2 <= 0:
                        continue
                    x = p1[X] + v1[X] * t1
                    y = p1[Y] + v1[Y] * t1
                    if AREA_MIN <= x <= AREA_MAX and AREA_MIN <= y <= AREA_MAX:
                        answer += 1
        return answer
    
    hailstones = read_input()
    return solve()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
