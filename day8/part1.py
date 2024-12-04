INPUT_FILE = "input.txt"

def solution(filename):
    with open(filename) as f:
        instr, _ = next(f).strip(), next(f)
        network = {}
        for line in f:
            node, conn = line.strip().split(" = ")
            network[node] = conn.strip("()").split(", ")
    instr = instr.replace("L", "0").replace("R", "1")
    
    def trace(node):
        steps = i = 0
        while node != "ZZZ":
            node = network[node][int(instr[i])]
            i = (i + 1) % len(instr)
            steps += 1
        return steps
    
    return trace("AAA")

if __name__ == "__main__":
    print(solution(INPUT_FILE))
