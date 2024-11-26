from node import Node


class Graph:

    def __init__(self):
        self.nodes: list[Node] = []
        self.node_dict = {}

    def add_node(self, x, y, flaminess):
        self.node_dict[(x, y)] = len(self.nodes)
        self.nodes.append(Node(x, y, flaminess))

    def add_edge(self, x1, y1, x2, y2):
        print("added edge")

        node_index1 = self.node_dict[(x1, y1)]
        node_index2 = self.node_dict[(x2, y2)]

        node1: Node = self.nodes[node_index1]
        node2: Node = self.nodes[node_index2]

        node1.add_neighbor(node2)
        node2.add_neighbor(node1)
