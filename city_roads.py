import numpy as np

np.random.seed(0)


class CGraph:
    # Initializer could be changed to take x, y and z domains, e.g. def __init__(self, [x_min, x_max], etc)
    def __init__(self):
        self.graph_dict = {}
        self.num_nodes = 0
        pass

    def add_node(self, node_id):
        self.num_nodes += 1
        # can later add handler to rare case when the coord already exists
        # x, y, z = np.random.randint(low=0, high=10 + 1, size=3)
        # between [0, 1.0) * 10
        x, y, z = np.round(np.random.random(size=3) * 10, 1)
        self.graph_dict[node_id] = {'coords': (x, y, z), 'edges': []}
        return node_id

    def add_edge(self, _from, _to):
        # Create nodes if they don't exist before creating edge
        [self.add_node(node) for node in [_from, _to] if node not in self.graph_dict]
        self.graph_dict[_from]['edges'] += [_to]
        pass

    def get_node_ids(self):
        return self.graph_dict.keys()

    def print_graph(self):
        # print nodes
        for node in self.graph_dict:
            print('{}, {}, {}'.format(*self.graph_dict[node]['coords']))
        # print edges
        for _from in self.graph_dict:
            if len(self.graph_dict[_from]['edges']) > 0:
                [print('{}, {}'.format(_from, _to)) for _to in self.graph_dict[_from]['edges']]
        pass

    pass


#################################################################################
#################################################################################


if __name__ == "__main__":

    n = 10  # number of nodes (graph complexity)
    g = CGraph()  # later could input x, y, z domains to instantiate class

    # Loop until n nodes created
    while g.num_nodes < n:
        # Create new node or take existing
        if g.num_nodes <= 1:
            _from = g.add_node(g.num_nodes)
        else:
            new_node = np.random.choice([True, False])
            if new_node:
                _from = g.add_node(g.num_nodes)
            else:
                _from = np.random.choice(list(g.get_node_ids()))
        pass

        # Create new edge
        if g.num_nodes >= 2:
            available_nodes = list(set(g.get_node_ids()) - {_from})
            # Check if edge exists, else create a new one
            edge_exists = True
            while edge_exists:
                _to = np.random.choice(available_nodes)
                if _to not in g.graph_dict[_from]['edges']:
                    edge_exists = False
                    g.add_edge(_from, _to)
                    print('egde generated! from={} to={}'.format(_from, _to))
    # Print graph
    g.print_graph()

    pass
