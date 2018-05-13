import numpy as np

np.random.seed(0)


class CGraph:
    # Initializer could be changed to take x, y and z domains, e.g. def __init__(self, [x_min, x_max], etc)
    def __init__(self):
        self.graph_dict = {}
        self.num_nodes = 0

    def add_node(self):
        node_id = self.num_nodes
        self.num_nodes += 1
        if node_id not in self.graph_dict:
            # can later add handler to rare case when the coord already exists
            # x, y, z = np.random.randint(low=0, high=10 + 1, size=3)
            x, y, z = np.round(np.random.random(size=3) * 10, 1)  # between [0, 1.0) * 10
            self.graph_dict[node_id] = {'coords': (x, y, z), 'edges': []}
        return node_id

    def add_edge(self, _from, _to):
        if _from not in self.graph_dict:
            self.add_node()
        if _to not in self.graph_dict:
            self.add_node()
        self.graph_dict[_from]['edges'] += [_to]

    def get_node_ids(self):
        return self.graph_dict.keys()

    def print_graph(self):
        for node in self.graph_dict:
            print('{}, {}, {}'.format(*self.graph_dict[node]['coords']))
        for node in self.graph_dict:
            if len(self.graph_dict[node]['edges']) > 0:
                [print('{}, {}'.format(node, edge)) for edge in self.graph_dict[node]['edges']]
        pass

    pass


#################################################################################
#################################################################################


if __name__ == "__main__":

    n = 10  # number of nodes (graph complexity)
    g = CGraph()  # later could input x, y, z domains to instantiate class

    while g.num_nodes < n:

        # Start if no nodes yet
        if g.num_nodes == 0:
            _from = g.add_node()
        else:
            # Generate new node or select random from existing ones
            new_node = np.random.choice([True, False])
            if new_node or g.num_nodes <= 1:
                _from = g.add_node()
            else:
                # select random node from existing ones
                _from = np.random.choice(list(g.get_node_ids()))
        pass

        # Create a new edge
        if g.num_nodes >= 2:
            # Check if edge exists, else create a new one
            edge_exists = True
            while edge_exists:
                # select random node from all others except the _from node
                available_nodes = list(set(g.get_node_ids()) - {_from})
                _to = np.random.choice(available_nodes)
                # Check if edge already in list and that it does not intersect others
                if _to not in g.graph_dict[_from]['edges']:
                    edge_exists = False
                    g.add_edge(_from, _to)
                    # print('i={}, egde generated! from={} to={}'.format(i, _from, _to))
    g.print_graph()

    pass
