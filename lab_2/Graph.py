from typing import List, Tuple, Optional
import matplotlib.pyplot as plt
import  networkx as nx

class Node:
    def __init__(self, name):
        self.name = name

class Edge:
    def __init__(self, start:Node, end:Node, distance:float=None, one_way=False):
        self.start:Node = start
        self.end:Node = end

        self.distance:float = distance
        self.one_way:bool = one_way

        self.max_auto_capacity = 400


class Graph:
    def __init__(self):
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []

    def add_node(self, name:str):
        self.nodes.append(Node(name))

    def add_edge(self, start:Node, end:Node, distance=None, one_way=False):
        self.edges.append(Edge(start, end, distance, one_way))

    def __getitem__(self, key:str) -> Optional[Node]:
        results = [el for el in self.nodes if el.name == key]
        if len(results) > 0:
            return  results[0]
        else: return None

    def draw(self):
        G = nx.Graph()

        for node in self.nodes:
            G.add_node(node.name)


        for edge in self.edges:
            G.add_edge(edge.start.name, edge.end.name, weight=edge.distance)

        node_positions = nx.spring_layout(G, iterations=90)

        nx.draw_networkx_nodes(G, node_positions, node_size=400, node_color=(.123, .3, .5))
        nx.draw_networkx_edges(G, node_positions, width=2, alpha=1, edge_color='gray')

        edge_labels = {(edge.start.name, edge.end.name): f"{edge.distance} km" for edge in self.edges}
        nx.draw_networkx_edge_labels(G, node_positions, edge_labels=edge_labels, font_color='red')

        node_labels = {node.name: node.name for node in self.nodes}
        nx.draw_networkx_labels(G, node_positions, labels=node_labels, font_size=8)

        plt.title('Connections between Places in Kyiv')
        plt.axis('off')
        plt.show()



