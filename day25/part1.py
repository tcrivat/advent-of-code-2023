"""
    The problem can be rephrased as finding a cut of size 3 in
an undirected graph.
    I use a randomized algorithm (Karger's algorithm) to find
cuts of small sizes in the graph. The algorithm takes the initial
graph and combines (contracts) edges, represented as pair of
nodes, until only two nodes are left in the graph. As there are
vastly less edges that are part of the min cut compared to the
total number of edges, it is far more likely for non min cut
edges to be randomly chosen.
    To choose an edge, I first uniformly choose one of the
remaining nodes (node1), then I choose one of the nodes adjacent
with the first node (node2). As the adjacency list may contain
duplicates of nodes (if there are multiple edges between the
nodes after previous contractions), the random choice of the
second node is in fact weighted by the number of edges (a node
with multiple edges connected to the first node has a greater
probability of being chosen).
    After contracting the edge (node1, node2), node2 will be
removed from the graph and all the node2's edges will be moved
to node1. This can result in multiple edges being present between
the same two nodes, which is expected.
    At the end of a run of the algorithm, only two nodes remain
in the graph. The number of edges between the two nodes represent
the size of the cut. If it is greater than 3, the algorithm is
repeated again on a new copy of the initial graph, until a cut of
size 3 is found.
"""
import copy, random
from collections import defaultdict

INPUT_FILE = "input.txt"

def solution(filename):
    def read_input():
        adj = defaultdict(list)
        with open(filename) as f:
            while line := f.readline().strip():
                node, adj_list = line.split(": ")
                for other in adj_list.split():
                    adj[node].append(other)
                    adj[other].append(node)
        return adj
    
    def min_cut_karger(adj):
        adj = copy.deepcopy(adj)
        count = {node: 1 for node in adj}
        while len(adj) > 2:
            node1 = random.choice(list(adj.keys()))
            node2 = random.choice(adj[node1])
            for other in adj[node2]:
                adj[other].remove(node2)
                if other != node1:
                    adj[node1].append(other)
                    adj[other].append(node1)
            count[node1] += count[node2]
            del adj[node2]
            del count[node2]
        group1, group2 = iter(adj)
        return len(adj[group1]), count[group1], count[group2]
    
    adj = read_input()
    cut = 4
    while cut > 3:
        cut, size1, size2 = min_cut_karger(adj)
        # print(cut, size1, size2)
    return size1 * size2

if __name__ == "__main__":
    print(solution(INPUT_FILE))

