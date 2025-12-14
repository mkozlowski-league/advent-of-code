class Node:
    def __init__(self, name):
        self.name = name
        self.sinks = []

nodes = {}
with open("day11input.txt", 'r') as file:
    for line in file:
        line = line.strip()

        source, destinations = line.split(':')
        destinations = destinations.lstrip().split(' ')

        n = nodes.setdefault(source, Node(source))
        dest_nodes = []
        for d in destinations:
            dn = nodes.setdefault(d, Node(d))
            dest_nodes.append(dn)
        n.sinks = dest_nodes

known_paths = {}
def flow(node):
    if len(node.sinks) == 0:
        return [node.name]
    if node.name in known_paths:
        return known_paths[node.name]

    paths = []
    for sink in node.sinks:
        sink_paths = flow(sink)
        paths.extend([node.name + p for p in sink_paths])
    known_paths[node.name] = paths
    return paths

paths = flow(nodes['you'])
out_paths = [p for p in paths if p.endswith('out')]
print(len(out_paths))