import numpy as np
np.random.seed(0)


class CGraph:

    def __init__(self):
        self.graph_dict = {}
        self.num_nodes = 0
        pass

    def add_node(self, node_id):
        # Should put boundary check
        x, y, z = np.round(np.random.random(size=3) * 10, 1)
        r = np.sqrt(x * x + y * y + z * z)
        if len(self.graph_dict) > 0:
            for node in self.graph_dict:
                x2, y2, z2 = self.graph_dict[node]['coords']
                r2 = np.sqrt(x2 * x2 + y2 * y2 + z2 * z2)
                diff = np.abs(r - r2)
                if diff < 2:
                    # If close, then return original node
                    return node
                else:
                    self.num_nodes += 1
                    self.graph_dict[node_id] = {'coords': (x, y, z), 'edges': []}
                    return node_id
        self.num_nodes += 1
        self.graph_dict[node_id] = {'coords': (x, y, z), 'edges': []}
        return node_id

    def add_edge(self, _from, _to):
        # create the nodes if they dont exist
        [self.add_node(node) for node in [_from, _to] if node not in self.graph_dict]
        self.graph_dict[_from]['edges'] += [_to]
        pass

    def get_nodes_ids(self):
        return self.graph_dict.keys()

    def print_graph(self):
        # Print node coords
        for node in self.graph_dict:
            print('{}, {}, {}'.format(*self.graph_dict[node]['coords']))
        # Print edges
        for _from in self.graph_dict:
            if len(self.graph_dict[_from]['edges']) > 0:
                for _to in self.graph_dict[_from]['edges']:
                    print('{}, {}'.format(_from, _to))
        pass


#######################################################

def select_to_node(g, _from):
    # Select node from new or existing
    new_node = np.random.choice([True, False])
    if not new_node:
        available_nodes = list(set(g.get_nodes_ids()) - {_from})
        _to = np.random.choice(available_nodes)
        # Ensure no duplicates
        if _to not in g.graph_dict[_from]['edges']:
            return _to
    _to = g.add_node(g.num_nodes)
    return _to


# Define number of nodes n and graph object
n = 20
g = CGraph()

# Loop until n reached
while g.num_nodes < n:

    # Define the _from node from existing
    if g.num_nodes <= 1:
        _from = g.add_node(g.num_nodes)
    else:
        _from = np.random.choice(list(g.get_nodes_ids()))
    pass

    # Define the _to node and then create edge with _from and _to
    if g.num_nodes >= 2:
        _to = select_to_node(g, _from)
        g.add_edge(_from, _to)
    pass

# Print the graph
g.print_graph()
