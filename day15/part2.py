"""
"""
INPUT_FILE = "input.txt"
MAX_BOXES = 256

def solution(filename):
    def read_input():
        with open(filename) as f:
            return f.readline().strip().split(",")
    
    def hash(string):
        answer = 0
        for c in string:
            answer = ((answer + ord(c)) * 17) % 256
        return answer
    
    def execute(op):
        if op[-1] == "-":
            label = op[:-1]
            box = hash(label)
            if label in boxes[box]:
                del boxes[box][label]
        else:
            label = op[:-2]
            focal_length = int(op[-1])
            box = hash(label)
            boxes[box][label] = focal_length
    
    def compute_focusing_power():
        return sum((box + 1) * (slot + 1) * focal_length
                   for box in range(MAX_BOXES)
                   for slot, focal_length in
                       enumerate(boxes[box].values()))
    
    operations = read_input()
    boxes = [{} for _ in range(MAX_BOXES)]
    for op in operations:
        execute(op)
    return compute_focusing_power()

if __name__ == "__main__":
    print(solution(INPUT_FILE))
