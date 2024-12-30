"""
"""
INPUT_FILE = "input.txt"

def solution(filename):
    def read_input():
        with open(filename) as f:
            return f.readline().strip().split(",")
    
    def hash(string):
        answer = 0
        for c in string:
            answer = ((answer + ord(c)) * 17) % 256
        return answer
    
    strings = read_input()
    return sum(hash(string) for string in strings)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
