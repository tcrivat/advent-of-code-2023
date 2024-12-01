import math

INPUT_FILE = "input.txt"

def solution(filename):
    with open(filename) as f:
        schematic = [line.rstrip() for line in f]
    N = len(schematic)
    M = len(schematic[0])
    
    def search_part_number(i, j, part_numbers):
        if (i < 0 or j < 0 or i >= N or j >= M
                or not schematic[i][j].isdigit()):
            return
        j1 = j
        while j1 > 0 and schematic[i][j1 - 1].isdigit():
            j1 -= 1
        j2 = j
        while j2 < M - 1 and schematic[i][j2 + 1].isdigit():
            j2 += 1
        number = int(schematic[i][j1:j2+1])
        part_numbers[(i, j1)] = number
    
    def update_part_numbers(i, j, part_numbers):
        search_part_number(i - 1, j - 1, part_numbers)
        search_part_number(i - 1, j, part_numbers)
        search_part_number(i - 1, j + 1, part_numbers)
        search_part_number(i, j - 1, part_numbers)
        search_part_number(i, j + 1, part_numbers)
        search_part_number(i + 1, j - 1, part_numbers)
        search_part_number(i + 1, j, part_numbers)
        search_part_number(i + 1, j + 1, part_numbers)
    
    answer = 0
    for i in range(N):
        for j in range(M):
            if schematic[i][j] == "*":
                part_numbers = {}
                update_part_numbers(i, j, part_numbers)
                if len(part_numbers) == 2:
                    answer += math.prod(part_numbers.values())
    return answer

if __name__ == "__main__":
    print(solution(INPUT_FILE))
