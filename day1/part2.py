import re

INPUT_FILE = "input.txt"
WORDS = {"one" : "1", "two" : "2", "three" : "3",
         "four" : "4", "five" : "5", "six" : "6",
         "seven" : "7", "eight" : "8", "nine" : "9"}
PATTERN1 = r"\d|one|two|three|four|five|six|seven|eight|nine"
PATTERN2 = r"\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin"

def to_digit(digit):
    return digit if digit[0].isdigit() else WORDS[digit]

def solve(line):
    first = re.search(PATTERN1, line).group(0)
    last = re.search(PATTERN2, line[::-1]).group(0)
    return int(to_digit(first) + to_digit(last[::-1]))

def solution(filename):
    with open(filename) as f:
        return sum(solve(line) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
