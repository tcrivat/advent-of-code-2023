import math

INPUT_FILE = "input.txt"

def get_rank(hand):
    jokers = hand.count("0")
    freq_dict = {c: hand.count(c) for c in hand}
    freq_list = sorted(map(str, freq_dict.values()))
    if 0 < jokers < 5:
        freq_list.remove(str(jokers))
        freq_list[-1] = str(int(freq_list[-1]) + jokers)
    freq_str = "".join(freq_list)
    strings = ["11111", "1112", "122", "113", "23", "14", "5"]
    return str(strings.index(freq_str) + 1)

def fix(hand):
    repl = {'T': 'A', 'J': 'B', 'Q': 'C',
            'K': 'D', 'A': 'E', 'J': '0'}
    hand = hand.translate(str.maketrans(repl))
    return get_rank(hand) + hand

def solution(filename):
    with open(filename) as f:
        hands = []
        for line in f:
            hand, bid = line.split()
            hands.append((fix(hand), int(bid)))
    hands.sort()
    answer = 0
    for i, hand in enumerate(hands):
        answer += (i + 1) * hand[1]
    return answer

if __name__ == "__main__":
    print(solution(INPUT_FILE))
