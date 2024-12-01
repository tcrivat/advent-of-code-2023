import re

INPUT_FILE = "input.txt"

def solve(line):
    first = re.search(r"\d", line).group(0)
    last = re.search(r"\d", line[::-1]).group(0)
    return int(first + last)

def solution(filename):
    with open(filename) as f:
        return sum(solve(line) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
