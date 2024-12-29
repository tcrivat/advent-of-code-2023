"""
    Dynamic Programming top-down solution (with memoization)
    solve(i, j, springs, groups) counts the possible arrangements
starting from index i in the springs string and index j in the
list of contiguous groups of damaged springs.
    To do this, it checks the current (with index i) character
in springs. If it's ".", it just ignores it, moving to the next
character. If it's "#", it tries to match the characters in the
next group of damaged springs. It it's "?", it considers both
possibilities ("?" replaced by "." or "#"), adding up the two
results. If index i is placed at the end of the springs string,
the function either returns 1 if there is no group of damaged
springs left, or 0 otherwise (this means some groups are left
unmatched).
    A separate function matches the number of characters in the
next group of damaged springs with the next characters in springs.
It can return a successful match only if there is still at least
a group to be matched, if there are enough characters left in
springs to accomodate the group and if all these characters are
either "#" or "?". After all these characters are tested, springs
either reaches the end or the next character is "." or "?", as
two different groups should be separated by at least a ".".
"""
INPUT_FILE = "input.txt"
MULTIPLIER = 5

def solution(filename):
    def read_input():
        with open(filename) as f:
            while line := f.readline().strip():
                springs, groups = line.split()
                springs = "?".join([springs] * MULTIPLIER)
                groups = ",".join([groups] * MULTIPLIER)
                groups = list(map(int, groups.split(",")))
                yield springs, groups
    
    def match(i, j, springs, groups):
        if j == len(groups) or i + groups[j] > len(springs):
            return 0
        
        for k in range(i, i + groups[j]):
            if springs[k] == ".":
                return 0
        
        if i + groups[j] == len(springs):
            return 1 if j + 1 == len(groups) else 0
        
        if springs[i + groups[j]] == "#":
            return 0

        return solve(i + groups[j] + 1, j + 1, springs, groups)
    
    def solve(i, j, springs, groups):
        if i == 0 and j == 0:
            memo.clear()
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(springs):
            answer = 1 if j == len(groups) else 0
        else:
            match springs[i]:
                case ".":
                    answer = solve(i + 1, j, springs, groups)
                case "#":
                    answer = match(i, j, springs, groups)
                case "?":
                    answer = (solve(i + 1, j, springs, groups)
                              + match(i, j, springs, groups))
        
        memo[(i, j)] = answer
        return answer
    
    memo = {}
    return sum(solve(0, 0, springs, groups)
               for springs, groups in read_input())

if __name__ == "__main__":
    print(solution(INPUT_FILE))
