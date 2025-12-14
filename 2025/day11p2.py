class Node:
    def __init__(self, name):
        self.name = name
        self.sinks = []
        self.sources = []

with open("day11input.txt", 'r') as file:
    nodes = {}
    for line in file:
        line = line.strip()

        source, destinations = line.split(':')
        destinations = destinations.lstrip().split(' ')

        n = nodes.setdefault(source, Node(source))
        dest_nodes = []
        for d in destinations:
            dn = nodes.setdefault(d, Node(d))
            dn.sources.append(n)
            dest_nodes.append(dn)
        n.sinks = dest_nodes

known_paths = {}
def flow(node, stop = None):
    if node.name in (stop or set()):
        return [node.name]
    if len(node.sinks) == 0:
        return [] # prune ends that didn't stop where we expected
    if node.name in known_paths:
        return known_paths[node.name]

    paths = []
    for sink in node.sinks:
        # Pretty sure there are no cycles but if there are this will stop it
        sink_paths = flow(sink, {node.name} | (stop or set()))
        paths.extend([node.name + p for p in sink_paths])
    known_paths[node.name] = paths
    return paths

# Through experimentation, concluded that there is likely no cycles and that the order will be:
# SVR -> FFT -> DAC -> OUT
# Calculate each section and multiply. Clear the function call cache to keep memory from exploding
print("Calculating fft -> out paths")
dac_out_paths = flow(nodes['dac'], {'out'})
do_len = len(dac_out_paths)
known_paths.clear()
dac_out_paths.clear()

print("Calculating fft -> dac paths")
fft_dac_paths = flow(nodes['fft'], {'dac'})
fd_len = len(fft_dac_paths)
known_paths.clear()
fft_dac_paths.clear()

print("Calculating svr -> fft paths")
svr_fft_paths = flow(nodes['svr'], {'fft'})
sf_len = len(svr_fft_paths)
known_paths.clear()
svr_fft_paths.clear()

print(do_len * fd_len * sf_len)
