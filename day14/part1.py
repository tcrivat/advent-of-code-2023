"""
    To tilt the platform towards the north, I iterate through
the columns from the north to the south and remember the position
of the last rock on that column. If I encounter a new fixed rock,
I set this as the pposition of the last rock; if the rock is round,
I move it immediately below the last position and increment the
last position.
"""
INPUT_FILE = "input.txt"

def solution(filename):
    def read_input():
        matrix = []
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(list(line))
        return matrix
    
    def tilt_north():
        for j in range(m):
            last_rock = -1
            for i in range(n):
                if matrix[i][j] == "#":
                    last_rock = i
                elif matrix[i][j] == "O":
                    last_rock += 1
                    matrix[i][j] = "."
                    matrix[last_rock][j] = "O"
    
    def count_load():
        return sum(row.count("O") * (n - i)
                   for i, row in enumerate(matrix))
    
    def print_map():
        for i in range(n):
            for j in range(m):
                print(matrix[i][j], end="")
            print()
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    tilt_north()
    # print_map()
    return count_load()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
