INPUT_FILE = "input.txt"

def solve(card):
    numbers = card.split(":")[1].split("|")
    set1 = set(numbers[0].split())
    set2 = set(numbers[1].split())
    return len(set1 & set2)

def solution(filename):
    instances = []
    with open(filename) as f:
        for i, card in enumerate(f):
            j1 = i + 1
            j2 = j1 + solve(card)
            if j2 > len(instances):
                instances += [1] * (j2 - len(instances))
            for j in range(j1, j2):
                instances[j] += instances[i]
    return sum(instances)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
