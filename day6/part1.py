import math

INPUT_FILE = "input.txt"

def solve(time, record):
    count = 0
    for i in range(time):
        if i * (time - i) > record:
            count += 1
    return count

def solution(filename):
    with open(filename) as f:
        line1, line2 = f
        times = map(int, line1.split()[1:])
        records = map(int, line2.split()[1:])
        races = zip(times, records)
        return math.prod(solve(t, r) for t, r in races)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
