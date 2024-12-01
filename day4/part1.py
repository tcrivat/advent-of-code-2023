INPUT_FILE = "input.txt"

def solve(card):
    numbers = card.split(":")[1].split("|")
    set1 = set(numbers[0].split())
    set2 = set(numbers[1].split())
    winning = len(set1 & set2)
    return 1 << (winning - 1) if winning else 0

def solution(filename):
    with open(filename) as f:
        return sum(solve(card) for card in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
