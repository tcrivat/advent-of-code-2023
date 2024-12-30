"""
    I tilt the platform in cycles and after each cycle, I
store the positions of all the stones on the platform. If
I encounter again a position that I saw before, it means
that the positions are repeating. I determine the period
with which the positions are repeating and finally determine
the answer by using the modulo operator.
"""
INPUT_FILE = "input.txt"
CYCLES = 1000000000

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
    
    def tilt_south():
        for j in range(m):
            last_rock = n
            for i in range(n - 1, -1, -1):
                if matrix[i][j] == "#":
                    last_rock = i
                elif matrix[i][j] == "O":
                    last_rock -= 1
                    matrix[i][j] = "."
                    matrix[last_rock][j] = "O"
    
    def tilt_west():
        for i in range(n):
            last_rock = -1
            for j in range(m):
                if matrix[i][j] == "#":
                    last_rock = j
                elif matrix[i][j] == "O":
                    last_rock += 1
                    matrix[i][j] = "."
                    matrix[i][last_rock] = "O"
    
    def tilt_east():
        for i in range(n):
            last_rock = m
            for j in range(m - 1, -1, -1):
                if matrix[i][j] == "#":
                    last_rock = j
                elif matrix[i][j] == "O":
                    last_rock -= 1
                    matrix[i][j] = "."
                    matrix[i][last_rock] = "O"
    
    def count_load():
        return sum(row.count("O") * (n - i)
                   for i, row in enumerate(matrix))
    
    def print_map():
        for i in range(n):
            for j in range(m):
                print(matrix[i][j], end="")
            print()
    
    def matrix_repr():
        return "".join("".join(row) for row in matrix)
    
    def solve():
        loads = []
        mappings = {}
        while True:
            tilt_north()
            tilt_west()
            tilt_south()
            tilt_east()
            # print()
            # print("After", len(loads) , "cycles:")
            # print_map()
            current_matrix = matrix_repr()
            if current_matrix in mappings:
                start = mappings[current_matrix]
                period = len(loads) - start
                return loads[period:] + loads[start:period]
            mappings[current_matrix] = len(loads)
            loads.append(count_load())
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    loads = solve()
    return loads[(CYCLES - 1) % len(loads)]

if __name__ == "__main__":
    print(solution(INPUT_FILE))
