"""
    I use two variables:
    - area = the total area of the excavated lagoon
    - width = the current width of the lagoon
    Initially both the area and the width are 1 (the matrix
representation of the lagoon contains only one '#' character).
    I then iterate through the input line by line and update
the two variables for each line in the input:
    - When digging to the rigth, the area is increased with the
digged distance (corresponding to the last <dist> '#' characters
in the current line of the matrix representation of the lagoon);
the width is also increased by the same distance.
    - When digging down, I increase the area with the distance
multiplied by the width (corresponding to the next <dist> lines
of width <width> containing the '#' characters in the matrix).
    - When digging left, the area is not updated, I just decrease
the width.
    - When diggind up, I decrease the area with the distance
multiplied by width-1 (corresponding to the previous <dist> lines
that start with <width-1> '.' characters in the matrix).
"""
INPUT_FILE = "input.txt"

def solution(filename):
    def read_input():
        with open(filename) as f:
            while line := f.readline():
                _, _, color = line.split()
                dir = int(color[7])
                dist = int(color[2:7], 16)
                yield dir, dist
    
    def solve():
        area = 1
        width = 1
        for dir, dist in read_input():
            match dir:
                case 0: # "R"
                    area += dist
                    width += dist
                case 1: # "D"
                    area += width * dist
                case 2: # "L"
                    width -= dist
                case 3: # "U"
                    area -= (width - 1) * dist
        return area
    
    return solve()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
