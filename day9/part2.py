INPUT_FILE = "input.txt"

def solution(filename):
    def solve(sequence):
        sign = 1
        answer = sequence[0]
        while any(sequence):
            sequence = [sequence[i] - sequence[i - 1]
                        for i in range(1, len(sequence))]
            sign *= -1
            answer += sign * sequence[0]
        return answer
    
    with open(filename) as f:
        return sum(solve(list(map(int, line.split()))) for line in f)

if __name__ == "__main__":
    print(solution(INPUT_FILE))

