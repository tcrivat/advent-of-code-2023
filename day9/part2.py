INPUT_FILE = "input.txt"

def solution(filename):
    def solve(numbers):
        sequences = [numbers]
        answer = numbers[0]
        sign = 1
        while any(sequences[-1]):
            last_sequence = sequences[-1]
            new_sequence = []
            for i in range(1, len(last_sequence)):
                new_sequence.append(last_sequence[i] - last_sequence[i - 1])
            sequences.append(new_sequence)
            sign *= -1
            answer += sign * new_sequence[0]
        return answer
    
    with open(filename) as f:
        return sum(solve(list(map(int, line.split()))) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))

