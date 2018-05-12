import numpy as np
import random
np.random.seed(0)

# class CNode:
#     def __init__(self, node_id):
#         self.id = node_id


class CGraph:
    # Initializer could be changed to take x, y and z domains, e.g. def __init__(self, [x_min, x_max], etc)
    def __init__(self):
        self.graph_dict = {}
        self.num_nodes = 0

    def add_node(self, node_id):
        self.num_nodes += 1
        if node_id not in self.graph_dict:
            x, y, z = np.random.randint(low=0, high=10 + 1, size=3)
            self.graph_dict[node_id] = {'coords': (x, y, z), 'edges': []}

    def add_edge(self, _from, _to):
        if _from not in self.graph_dict:
            self.add_node(_from)
        if _to not in self.graph_dict:
            self.add_node(_to)
        self.graph_dict[_from]['edges'] += [_to]

    def get_graph(self):
        return self.graph_dict

    def print_graph(self):
        for node in self.graph_dict:
            print('{}, {}, {}'.format(*self.graph_dict[node]['coords']))
        for node in self.graph_dict:
            if len(self.graph_dict[node]['edges']) > 0:
                [print('{}, {}'.format(node, edge)) for edge in self.graph_dict[node]['edges']]
        pass


#################################################################################
#################################################################################


if __name__ == "__main__":

    # g = CGraph()
    # g.add_edge(0, 1)
    # g.add_edge(1, 2)
    # g.print_graph()

    pass
