INPUT_FILE = "input.txt"

def solution(filename):
    items = []
    transformed = []
    first_line = True
    with open(filename) as f:
        for line in f:
            if first_line:
                items = list(map(int, line.split(":")[1].split()))
                first_line = False
            elif line.strip() == "":
                continue
            elif "map" in line:
                transformed = [False] * len(items)
            else:
                dest, src, length = map(int, line.split())
                for i in range(len(items)):
                    if transformed[i]:
                        continue # already transformed during this round
                    if src <= items[i] < src + length:
                        items[i] = dest + items[i] - src
                        transformed[i] = True
    return min(items)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
