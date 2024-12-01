import math

INPUT_FILE = "input.txt"

def update_max(round, max_cubes):
    for pair in round.split(","):
        count, color = pair.strip().split();
        max_cubes[color] = max(max_cubes[color], int(count))

def solve(line):
    game, rounds = line.split(":")
    max_cubes = { "red": 0, "green": 0, "blue": 0 }
    for round in rounds.split(";"):
        update_max(round, max_cubes)
    return math.prod(max_cubes.values())

def solution(filename):
    with open(filename) as f:
        return sum(solve(line) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
