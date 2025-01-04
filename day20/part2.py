"""
    By looking at the input data I observed that the penultimate
module (before the last which is the output module) is of the
conjunction type. This means that it will send a low pulse to the
ultimate (output) node only when all of its own inputs send a high
pulse.
    So I start pressing the button and watch all these inputs
(called the antepenultimates). For each of them I store in a list
(results) the minimum number of button presses after which these
nodes send a high pulse.
    The solution is the least common multiple of these numbers, as
all these nodes need to send a high pulse at the same time.
"""
import math
from collections import deque

INPUT_FILE = "input.txt"
OUTPUT_NODE = "rx"
LOW = False
HIGH = True

def solution(filename):
    def read_input():
        adj = {}
        types = {}
        with open(filename) as f:
            while line := f.readline().strip():
                node, destinations = line.split(" -> ")
                if node[0] in ["%", "&"]:
                    types[node[1:]] = node[0]
                    node = node[1:]
                adj[node] = destinations.split(", ")
        return adj, types
    
    def initial_state():
        state = {}
        penultimate_node = None
        for node in adj:
            if types.get(node) == "%":
                state[node] = LOW
            for dest in adj[node]:
                if types.get(dest) == "&":
                    node_dict = state.setdefault(dest, {})
                    node_dict[node] = LOW
                elif dest == OUTPUT_NODE:
                    assert penultimate_node == None
                    assert types.get(node) == "&"
                    penultimate_node = node
        return state, penultimate_node
    
    def send(node, pulse, queue):
        if node in antepenultimates and pulse == HIGH:
            results[node] = cycles
        for dst_node in adj[node]:
            queue.append((node, dst_node, pulse))
    
    def push_button():
        queue = deque([("button", "broadcaster", LOW)])
        while queue:
            src_node, node, pulse = queue.popleft()
            if node == "broadcaster":
                send(node, pulse, queue)
            elif types.get(node) == "%" and pulse == LOW:
                state[node] = not state[node]
                send(node, state[node], queue)
            elif types.get(node) == "&":
                state[node][src_node] = pulse
                pulse = not all(state[node].values())
                send(node, pulse, queue)
    
    adj, types = read_input()
    state, penultimate = initial_state()
    antepenultimates = state[penultimate]
    results = {}
    cycles = 0
    while len(results) < len(antepenultimates):
        cycles += 1
        push_button()
    return math.lcm(*results.values())

if __name__ == "__main__":
    print(solution(INPUT_FILE))
