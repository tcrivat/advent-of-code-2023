import re, math

INPUT_FILE = "input.txt"

def solution(filename):
    with open(filename) as f:
        schematic = [line.rstrip() for line in f]
    N = len(schematic)
    M = len(schematic[0])
    
    def is_simbol(i, j):
        if i < 0 or j < 0 or i >= N or j >= M:
            return False
        return (not schematic[i][j].isdigit() and
               schematic[i][j] != ".")
    
    def touches_symbol(i, j):
        return (is_simbol(i - 1, j - 1) or
               is_simbol(i - 1, j) or
               is_simbol(i - 1, j + 1) or
               is_simbol(i, j - 1) or
               is_simbol(i, j + 1) or
               is_simbol(i + 1, j - 1) or
               is_simbol(i + 1, j) or
               is_simbol(i + 1, j + 1))
    
    answer = 0
    for i in range(N):
        carry = 0
        is_part_number = False
        for j in range(M):
            if schematic[i][j].isdigit():
                carry *= 10
                carry += int(schematic[i][j])
                is_part_number = is_part_number or touches_symbol(i, j)
                if (is_part_number and
                    (j == M - 1 or not schematic[i][j + 1].isdigit())):
                    answer += carry
            else:
                carry = 0
                is_part_number = False
    return answer

if __name__ == "__main__":
    print(solution(INPUT_FILE))
