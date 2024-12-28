"""
    expansions[0][i] = the number of expansions between line 0 and line i
    expansions[1][j] = the number of expansions between column 0 and column j
"""
INPUT_FILE = "input.txt"
EXPANSIONS = 2

def solution(filename):
    def read_input():
        matrix = []
        with open(filename) as f:
            while line := f.readline().strip():
                matrix.append(line)
        return matrix
    
    def find_galaxies():
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "#":
                    yield i, j
    
    def find_expansions():
        expansions = [[0] * n, [0] * m]
        for i in range(n):
            if i > 0:
                expansions[0][i] = expansions[0][i - 1]
            if "#" not in matrix[i]:
                expansions[0][i] += EXPANSIONS - 1
        for j in range(m):
            if j > 0:
                expansions[1][j] = expansions[1][j - 1]
            if "#" not in [matrix[i][j] for i in range(n)]:
                expansions[1][j] += EXPANSIONS - 1
        return expansions
    
    def distance(galaxy1, galaxy2):
        return (abs(galaxy1[0] - galaxy2[0]) +
                abs(expansions[0][galaxy1[0]] - expansions[0][galaxy2[0]]) +
                abs(galaxy1[1] - galaxy2[1]) +
                abs(expansions[1][galaxy1[1]] - expansions[1][galaxy2[1]]))
    
    def compute_answer():
        return sum(distance(galaxies[i], galaxies[j])
                   for i in range(len(galaxies))
                   for j in range(i))
    
    matrix = read_input()
    n = len(matrix)
    m = len(matrix[0])
    galaxies = list(find_galaxies())
    expansions = find_expansions()
    return compute_answer()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
