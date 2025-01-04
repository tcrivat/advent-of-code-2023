"""
    For every flip-flop or conjunction module (node) I keep its
required state:
    - for a flip-flop module, I keep only one state: on/off
    - for a conjunction module, I keep a dict containing the last
pulse sent by each of its inputs
    Pushing the button leads to a series of pulses being sent
between the modules/nodes. To make sure that the pulses are
processed by the modules in the correct order, I use a queue
(like a BFS traversal).
    I push the button 1000 times and keep the results in a list
with two elements (number of low and high pulses being sent),
updating this list every time a module sends a pulse to another
module.
"""
from collections import deque

INPUT_FILE = "input.txt"
CYCLES = 1000
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
        for node in adj:
            if types.get(node) == "%":
                state[node] = LOW
            for dest in adj[node]:
                if types.get(dest) == "&":
                    node_dict = state.setdefault(dest, {})
                    node_dict[node] = LOW
        return state
    
    def send(node, pulse, queue):
        for dst_node in adj[node]:
            queue.append((node, dst_node, pulse))
        results[pulse] += len(adj[node])
    
    def push_button():
        results[LOW] += 1 # button -> broadcaster
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
    state = initial_state()
    results = [0, 0]
    for _ in range(CYCLES):
        push_button()
    return results[LOW] * results[HIGH]

if __name__ == "__main__":
    print(solution(INPUT_FILE))
