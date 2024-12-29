"""
    I represent "." as 0 and "#" as 1 and treat these as bits. A row in the matrix
will represent a number, a column in the matrix could represent a number as well.
So the matrix could be represented as a list of numbers, either horizontally or
vertically.
    To identify a reflection in this list, I start from every position between two
elements and check if the numbers at distance 0, 1, 2... from that position are equal.
This time, I allow one single mistake of 1 bit between these pairs of two numbers
(the "smudge"). To determine whether the numbers differ by one bit, I XOR the numbers
and count the number of bits in the result.
"""
INPUT_FILE = "input.txt"

def solution(filename):
    def read_input():
        with open(filename) as f:
            matrix = [None]
            while matrix:
                matrix = []
                while line := f.readline().strip():
                    line = line.replace(".", "0").replace("#", "1")
                    matrix.append(line)
                if matrix:
                    yield matrix
    
    def reflection(numbers):
        for i in range(1, len(numbers)):
            used_smudge = False
            for j in range(min(i, len(numbers) - i)):
                n1 = numbers[i - j - 1]
                n2 = numbers[i + j]
                if n1 != n2:
                    if not used_smudge and (n1 ^ n2).bit_count() == 1:
                        used_smudge = True
                    else:
                        break
            else:
                if used_smudge:
                    return i
        return 0
    
    def solve(matrix):
        cols = len(matrix[0])
        vertical = [int("".join(row[i] for row in matrix), 2) for i in range(cols)]
        horizontal = [int(row, 2) for row in matrix]
        return reflection(vertical) + 100 * reflection(horizontal)
    
    return sum(solve(matrix)
               for matrix in read_input())

if __name__ == "__main__":
    print(solution(INPUT_FILE))
