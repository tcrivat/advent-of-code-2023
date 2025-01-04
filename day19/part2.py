"""
    I execute the workflows with a special part that keeps track
of the minimum and maximum values for each category that are required
in order to enter a specific path in the workflow.
    When checking a rule, two divergent paths with two different such
parts are created, one for each branch. The results from the two paths
are added together.
    When a part is accepted, the call returns the product of the number
of possible values in each category or zero if the part is rejected.
"""
import math

INPUT_FILE = "input.txt"
MIN_VALUE = 1
MAX_VALUE = 4000

def solution(filename):
    def read_input():
        workflows = {}
        with open(filename) as f:
            while line := f.readline().strip():
                name, rules = line.strip("}").split("{")
                workflows[name] = []
                for rule_str in rules.split(","):
                    rule = {}
                    if ":" in rule_str:
                        expr, rule["target"] = rule_str.split(":")
                        rule["category"] = expr[0]
                        rule["op"] = expr[1]
                        rule["value"] = int(expr[2:])
                    else:
                        rule["op"] = "="
                        rule["target"] = rule_str
                    workflows[name].append(rule)
        return workflows
    
    def count(part, workflow):
        if workflow == "A":
            return math.prod(v2 - v1 + 1 for v1, v2 in part.values())
        elif workflow == "R":
            return 0
        
        answer = 0
        for rule in workflows[workflow]:
            match rule["op"]:
                case "<":
                    v = rule["value"]
                    v1, v2 = part[rule["category"]]
                    if v1 < v:
                        part2 = part.copy()
                        part2[rule["category"]] = (v1, min(v - 1, v2))
                        answer += count(part2, rule["target"])
                    if v2 < v:
                        break
                    part[rule["category"]] = (max(v, v1), v2)
                case ">":
                    v = rule["value"]
                    v1, v2 = part[rule["category"]]
                    if v2 > v:
                        part2 = part.copy()
                        part2[rule["category"]] = (max(v + 1, v1), v2)
                        answer += count(part2, rule["target"])
                    if v1 > v:
                        break
                    part[rule["category"]] = (v1, min(v, v2))
                case "=":
                    answer += count(part, rule["target"])
        return answer
    
    workflows = read_input()
    part = {key: (MIN_VALUE, MAX_VALUE) for key in "xmas"}
    return count(part, "in")

if __name__ == "__main__":
    print(solution(INPUT_FILE))
