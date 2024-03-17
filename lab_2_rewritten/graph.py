import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from config import Config
from collections import defaultdict


class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.labels = [None] * num_nodes 
        self.distances = np.full((num_nodes, num_nodes), np.inf)
        self.flows = np.zeros((num_nodes, num_nodes))
        for i in range(num_nodes):
            self.distances[i][i] = 0

    def add_edge(self, u, v, distance, flow):
        self.distances[u][v] = distance
        self.distances[v][u] = distance
        self.flows[u][v] = flow
        self.flows[v][u] = flow

    def remove_edge(self, u, v):
        self.distances[u][v] = np.inf
        self.distances[v][u] = np.inf
        self.flows[u][v] = 0
        self.flows[v][u] = 0

    def get_distance(self, u, v):
        return self.distances[u][v]

    def get_flow(self, u, v):
        return self.flows[u][v]

    def set_flow(self, u, v, flow):
        self.flows[u][v] = flow
        self.flows[v][u] = -flow
    
    
    def set_label(self, node, label):
        self.labels[node] = label

    def get_label(self, node):
        return self.labels[node]

    def minimum_spanning_tree(self):
        parent = list(range(self.num_nodes))
        rank = [0] * self.num_nodes 

        def find(x):
            """Find the root of the set containing x"""
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            """Union two sets containing x and y"""
            x_root = find(x)
            y_root = find(y)
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

        edges = []
        for u in range(self.num_nodes):
            for v in range(u + 1, self.num_nodes):
                if self.distances[u][v] != np.inf:
                    edges.append((self.distances[u][v], u, v))

        edges.sort()

        mst = []
        total_weight = 0
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v))
                total_weight += weight

        return mst, total_weight


class GraphOperations:

    @staticmethod
    def graph_coloring(graph):
        colors = {}
        
        available_colors = [i for i in range(graph.num_nodes)]
        neighbors = defaultdict(list)
        for u in range(graph.num_nodes):
            for v in range(graph.num_nodes):
                if graph.get_distance(u, v) < float('inf'):
                    neighbors[u].append(v)

        for node in range(graph.num_nodes):
            used_colors = set([colors.get(neighbor, None) for neighbor in neighbors[node]])
            for color in available_colors:
                if color not in used_colors:
                    colors[node] = color
                    break
        
        return colors


    @staticmethod
    def dijkstra(graph, source):
        num_nodes = graph.num_nodes
        distances = np.full(num_nodes, np.inf)
        distances[source] = 0
        visited = [False] * num_nodes
        parent = [-1] * num_nodes

        pq = [(0, source)]

        while pq:
            current_dist, current_node = pq.pop(0)

            if visited[current_node]:
                continue

            visited[current_node] = True

            for neighbor in range(num_nodes):
                if graph.get_distance(current_node, neighbor) < np.inf and graph.get_flow(current_node, neighbor) > 0:
                    distance = current_dist + graph.get_distance(current_node, neighbor)
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        parent[neighbor] = current_node
                        pq.append((distance, neighbor))

        return distances, parent


    @classmethod
    def ford_fulkerson(cls, graph, source, sink):
        num_nodes = graph.num_nodes
        max_flow = 0

        while True:
            distances, parent = cls.dijkstra(graph, source)
            if distances[sink] == np.inf:
                break

            min_flow = np.inf
            node = sink

            while node != source:
                parent_node = parent[node]
                min_flow = min(min_flow, graph.get_flow(parent_node, node))
                node = parent_node

            node = sink
            while node != source:
                parent_node = parent[node]
                graph.set_flow(parent_node, node, graph.get_flow(parent_node, node) - min_flow)
                node = parent_node

            max_flow += min_flow

        return max_flow


    @staticmethod
    def draw_graph(graph):
        G = nx.Graph()
        G.add_nodes_from(range(graph.num_nodes))

        for u in range(graph.num_nodes):
            for v in range(u + 1, graph.num_nodes):
                if graph.distances[u][v] != np.inf:
                    G.add_edge(u, v, weight=graph.distances[u][v])

        pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, pos, node_size=700)
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
        labels = {node: graph.get_label(node) for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='black')

        edge_labels = {(u, v): f"{graph.distances[u][v]:.2f}" for u, v in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Graph")
        plt.axis("off")
        plt.savefig(Config.output_dir + 'graph.png')
        plt.show()


    @staticmethod
    def draw_spanning_tree(graph, mst_edges):
        G = nx.Graph()
        labels = {}
        for edge in mst_edges:
            u, v = edge
            G.add_edge(u, v)
            labels[(u, v)] = graph.get_distance(u, v)  
            labels[(v, u)] = graph.get_distance(u, v)  

        pos = nx.spring_layout(G)  
        nx.draw_networkx_nodes(G, pos, node_size=700)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, labels={node: graph.get_label(node) for node in G.nodes()})  
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Minimum Spanning Tree")
        plt.axis("off")
        plt.savefig(Config.output_dir + 'minimum_spanning_tree.png')
        plt.show()