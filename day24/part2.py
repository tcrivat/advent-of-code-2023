"""
    This time the stone needs to intersect the trajectories of all the
hailstones, at the same time the hailstone is there!
    So if the stone has:
                 x y z @ vx vy vz
and the hailstone has:
        p[X] p[Y] p[Z] @ v[X] v[Y] v[Z]
    Their trajectories will need to cross at the same time. So:
        p[X] + v[X] * t1 = x + vx * t1
        p[Y] + v[Y] * t1 = y + vy * t1
        p[Z] + v[Z] * t1 = z + vz * t1
    Solving for t1 in the last equation gives:
        t1 = (z - p[Z]) / (v[Z] - vz)
    Replacing t1 in the first ecuation:
        p[X] + v[X] * (z - p[Z]) / (v[Z] - vz) =
            x + vx * (z - p[Z]) / (v[Z] - vz)
    Rearranging the terms gives:
        x * vz - z * vx - v[Z] * x + v[X] * z + p[Z] * vx
               - p[X] * vz + p[X] * v[Z] - v[X] * p[Z] = 0
    Similarly for the second ecuation:
        y * vz - z * vy - v[Z] * y + v[Y] * z + p[Z] * vy
               - p[Y] * vz + p[Y] * v[Z] - v[Y] * p[Z] = 0
    I put two such ecuations for each hailstone in a solver and
solve for x, y, z, vx, vy, vz. Only x, y, z are needed.
"""
import numpy
from scipy.optimize import root
numpy.seterr(over='ignore')

INPUT_FILE = "input.txt"
AREA_MIN = 200000000000000
AREA_MAX = 400000000000000
X = 0
Y = 1
Z = 2

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
    
    def equations(vars):
        x, y, z, vx, vy, vz = vars
        eq = []
        for p, v in hailstones:
            eq.append(x * vz - z * vx - v[Z] * x + v[X] * z + p[Z] * vx
                             - p[X] * vz + p[X] * v[Z] - v[X] * p[Z])
            eq.append(y * vz - z * vy - v[Z] * y + v[Y] * z + p[Z] * vy
                             - p[Y] * vz + p[Y] * v[Z] - v[Y] * p[Z])
        return eq
    
    hailstones = read_input()
    initial_guess = [(AREA_MIN + AREA_MAX) // 2] * 6
    result = root(equations, initial_guess, method='lm').x
    return sum(map(int, result[:3]))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
