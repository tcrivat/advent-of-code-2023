import math

INPUT_FILE = "input.txt"

def solve(time, record):
    delta = time ** 2 - 4 * record
    if delta < 0:
        return 0
    sol1 = math.ceil((time - math.sqrt(delta)) / 2)
    sol2 = math.floor((time + math.sqrt(delta)) / 2)
    return sol2 - sol1 + 1

def solution(filename):
    with open(filename) as f:
        line1, line2 = f
        time = int(line1.split(":")[1].replace(" ", ""))
        record = int(line2.split(":")[1].replace(" ", ""))
        return solve(time, record)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
