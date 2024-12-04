import math

INPUT_FILE = "input.txt"

def solution(filename):
    with open(filename) as f:
        instr, _ = next(f).strip(), next(f)
        network = {}
        for line in f:
            node, conn = line.strip().split(" = ")
            network[node] = conn.strip("()").split(", ")
    instr = instr.replace("L", "0").replace("R", "1")
    start = [node for node in network if node[-1] == "A"]
    
    def trace(node):
        steps = i = 0
        while node[-1] != "Z":
            node = network[node][int(instr[i])]
            i = (i + 1) % len(instr)
            steps += 1
        return steps
    
    return math.lcm(*(trace(node) for node in start))

if __name__ == "__main__":
    print(solution(INPUT_FILE))
