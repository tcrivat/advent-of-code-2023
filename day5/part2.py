INPUT_FILE = "input.txt"

def solution(filename):
    start = []
    end = []
    transformed = []
    first_line = True
    with open(filename) as f:
        for line in f:
            if first_line:
                items = line.split(":")[1].split()
                for i in range(len(items)):
                    if i % 2 == 1:
                        s = int(items[i - 1])
                        l = int(items[i])
                        start.append(s)
                        end.append(s + l - 1)
                first_line = False
            elif line.strip() == "":
                continue
            elif "map" in line:
                transformed = [False] * len(start)
            else:
                dest_start, src_start, length = map(int, line.split())
                src_end = src_start + length - 1
                for i in range(len(start)):
                    if transformed[i]:
                        continue # already transformed during this round
                    if end[i] < src_start or src_end < start[i]:
                        continue # disjoint intervals
                    if start[i] < src_start: # remaining to the left
                        start.append(start[i])
                        end.append(src_start - 1)
                        transformed.append(False)
                        start[i] = src_start
                    if src_end < end[i]: # remaining to the right
                        start.append(src_end + 1)
                        end.append(end[i])
                        transformed.append(False)
                        end[i] = src_end
                    start[i] = dest_start + start[i] - src_start
                    end[i] = dest_start + end[i] - src_start
                    transformed[i] = True
    return min(start)

if __name__ == "__main__":
    print(solution(INPUT_FILE))
