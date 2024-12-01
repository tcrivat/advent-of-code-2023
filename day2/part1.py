INPUT_FILE = "input.txt"
MAX_CUBES = { "red": 12, "green": 13, "blue": 14 }

def possible(round):
    for pair in round.split(","):
        count, color = pair.strip().split();
        if int(count) > MAX_CUBES[color]:
            return False
    return True

def solve(line):
    game, rounds = line.split(":")
    game_number = int(game.split()[1])
    for round in rounds.split(";"):
        if not possible(round):
            return 0
    return game_number

def solution(filename):
    with open(filename) as f:
        return sum(solve(line) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
