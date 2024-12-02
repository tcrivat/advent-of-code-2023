import math

INPUT_FILE = "input.txt"

def get_rank(hand):
    freq_dict = {c: hand.count(c) for c in hand}
    freq_str = "".join(sorted(map(str, freq_dict.values())))
    strings = ["11111", "1112", "122", "113", "23", "14", "5"]
    return str(strings.index(freq_str) + 1)

def fix(hand):
    repl = {'T': 'A', 'J': 'B', 'Q': 'C',
            'K': 'D', 'A': 'E'}
    hand = hand.translate(str.maketrans(repl))
    return get_rank(hand) + hand

def solution(filename):
    with open(filename) as f:
        hands = []
        for line in f:
            hand, bid = line.split()
            hands.append((fix(hand), int(bid)))
    hands.sort(key=lambda x: x[0])
    answer = 0
    for i, hand in enumerate(hands):
        answer += (i + 1) * hand[1]
    return answer

if __name__ == "__main__":
    print(solution(INPUT_FILE))
