"""
    I simply parse the input and execute the workflows for each part,
as instructed in the problem's statement.
"""
INPUT_FILE = "input.txt"

def solution(filename):
    def read_input():
        workflows = {}
        parts = []
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
            while line := f.readline().strip():
                part = {}
                for rating in line.strip("{}").split(","):
                    category, value = rating.split("=")
                    part[category] = int(value)
                parts.append(part)
        return workflows, parts
    
    def execute(part, workflow):
        for rule in workflows[workflow]:
            match rule["op"]:
                case "<":
                    if part[rule["category"]] < rule["value"]:
                        return rule["target"]
                case ">":
                    if part[rule["category"]] > rule["value"]:
                        return rule["target"]
                case "=":
                    return rule["target"]
    
    def check(part):
        workflow = "in"
        while (workflow not in ["A", "R"]):
            workflow = execute(part, workflow)
        return sum(part.values()) if workflow == "A" else 0
    
    workflows, parts = read_input()
    return sum(check(part) for part in parts)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
