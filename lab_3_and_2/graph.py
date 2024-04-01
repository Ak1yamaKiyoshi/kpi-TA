import matplotlib.pyplot as plt
import networkx as nx
from typing import Tuple, List
import numpy as np
from config import Config
from collections import defaultdict


class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.distances = np.full((num_nodes, num_nodes), np.inf)
        self.labels = [i for i in range(num_nodes)] 
        
        self._positions = [None] * num_nodes
        self.flows = np.zeros((num_nodes, num_nodes))
        for i in range(num_nodes):
            self.distances[i][i] = 0
        self._position = (None, None)


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
    
    def set_pos(self, node:int, pos: Tuple[int, int]):
        self._positions[node] = pos

    def get_pos(self, node):
        return self._positions[node]



class GraphOperations:
    
    @staticmethod
    def minimum_spanning_tree(graph):
        parent = list(range(graph.num_nodes))
        rank = [0] * graph.num_nodes 

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
        for u in range(graph.num_nodes):
            for v in range(u + 1, graph.num_nodes):
                if graph.distances[u][v] != np.inf:
                    edges.append((graph.distances[u][v], u, v))

        edges.sort()

        mst = []
        total_weight = 0
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v))
                total_weight += weight

        return mst, total_weight


    @classmethod
    def dfs(cls, graph: Graph, node, visited, stack):
        visited[node] = True
        for neighbor in range(graph.num_nodes):
            if graph.distances[node][neighbor] != np.inf and not visited[neighbor]:
                cls.dfs(graph, neighbor, visited, stack)
        stack.append(node)


    @staticmethod
    def transpose(graph):
        transposed_graph = Graph(graph.num_nodes)
        for i in range(graph.num_nodes):
            for j in range(graph.num_nodes):
                if graph.distances[i][j] != np.inf:
                    transposed_graph.add_edge(j, i, graph.distances[i][j], graph.flows[i][j])
        return transposed_graph


    @classmethod
    def algorythm_component_silnoji_zviyaznosty_po_shlyahah(cls, graph):
        visited = [False] * graph.num_nodes
        stack = []
        for i in range(graph.num_nodes):
            if not visited[i]:
                cls.dfs(graph, i, visited, stack)

        transposed_graph = cls.transpose(graph)

        visited = [False] * graph.num_nodes

        scc_list = []
        while stack:
            current_node = stack.pop()
            if not visited[current_node]:
                scc = []
                cls.dfs(transposed_graph, current_node, visited, scc)
                scc_list.append(scc)

        return scc_list


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
    def ford_fulkerson(cls, graph, source, sink, return_path = False):
        num_nodes = graph.num_nodes
        max_flow = 0
        paths = []

        while True:
            distances, parent = cls.dijkstra(graph, source)
            if distances[sink] == np.inf:
                break

            min_flow = np.inf
            node = sink
            path = []
            while node != source:
                parent_node = parent[node]
                min_flow = min(min_flow, graph.get_flow(parent_node, node))
                path.append((parent_node, node))
                node = parent_node

            paths.append(path)
            node = sink
            while node != source:
                parent_node = parent[node]
                graph.set_flow(parent_node, node, graph.get_flow(parent_node, node) - min_flow)
                node = parent_node

            max_flow += min_flow

        if return_path:
            return max_flow, paths
        return max_flow


    @classmethod
    def tarjan_scc(cls, graph: Graph):
        graph.index = 0
        graph.stack = []
        graph.scc_list = []
        graph.index_tracker = [None] * graph.num_nodes
        graph.low_link = [None] * graph.num_nodes
        graph.on_stack = [False] * graph.num_nodes

        for node in range(graph.num_nodes):
            if graph.index_tracker[node] is None:
                cls.tarjan_dfs(graph, node)

        return graph.scc_list


    @classmethod
    def tarjan_dfs(cls, graph, node):
        graph.index_tracker[node] = graph.index
        graph.low_link[node] = graph.index
        graph.index += 1
        graph.stack.append(node)
        graph.on_stack[node] = True

        for neighbor in range(graph.num_nodes):
            if graph.get_distance(node, neighbor) != np.inf:
                if graph.index_tracker[neighbor] is None:
                    cls.tarjan_dfs(graph, neighbor)
                    graph.low_link[node] = min(graph.low_link[node], graph.low_link[neighbor])
                elif graph.on_stack[neighbor]:
                    graph.low_link[node] = min(graph.low_link[node], graph.index_tracker[neighbor])

        if graph.low_link[node] == graph.index_tracker[node]:
            scc = []
            while True:
                top = graph.stack.pop()
                graph.on_stack[top] = False
                scc.append(top)
                if top == node:
                    break
            graph.scc_list.append(scc)

    # Перейменована хрінь по-суті
    @classmethod
    def find_scc_path_based(cls, graph):
        graph.index = 0
        graph.index_tracker = [None] * graph.num_nodes
        graph.low_link = [None] * graph.num_nodes
        graph.scc_list = []
        graph.stack = []

        for node in range(graph.num_nodes):
            if graph.index_tracker[node] is None:
                cls.explore_scc(graph, node)

        return graph.scc_list

    @classmethod
    def explore_scc(cls,  graph, node):
        graph.index_tracker[node] = graph.index
        graph.low_link[node] = graph.index
        graph.index += 1
        graph.stack.append(node)

        for neighbor in range(graph.num_nodes):
            if graph.get_distance(node, neighbor) != np.inf:
                if graph.index_tracker[neighbor] is None:
                    cls.explore_scc(graph, neighbor)
                if neighbor in graph.stack:
                    graph.low_link[node] = min(graph.low_link[node], graph.index_tracker[neighbor])

        if graph.low_link[node] == graph.index_tracker[node]:
            scc = []
            while True:
                top = graph.stack.pop()
                scc.append(top)
                if top == node:
                    break
            graph.scc_list.append(scc)
        return graph.scc_list


    @staticmethod
    def draw_kiyv_map(kiyv_map:Graph, label="kiyv_map", paths:List[List[Tuple[int, int]]]=[], scc=[]):
        G = nx.Graph()
        G.add_nodes_from(range(kiyv_map.num_nodes))

        for u in range(kiyv_map.num_nodes):
            for v in range(u + 1, kiyv_map.num_nodes):
                if kiyv_map.distances[u][v] != np.inf:
                    G.add_edge(u, v, weight=kiyv_map.distances[u][v])
                    
        pos = nx.spring_layout(G)
        colors = ["tab:red", "tab:blue", "tab:green", "yellow", "orange", "indigo"] * 10 
        
        for node in range(kiyv_map.num_nodes):
            pos[node] = np.array(kiyv_map.get_pos(node))
            try:
                print(node)
            except:
                pass

        nx.draw_networkx_nodes(G, pos, node_size=400)
        for lst, color in zip(scc, colors):
            nx.draw_networkx_nodes(G, pos, lst, node_size=400, node_color=color)
        
        nx.draw_networkx_edges(G,  pos,  width=0.8, alpha=0.8, arrows=True)
        for path, color in zip(paths, colors):
            nx.draw_networkx_edges(G, pos, edgelist=path,width=5, edge_color=color)
            
        labels = {node: kiyv_map.get_label(node) for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels, font_size=9, font_color='black')

        edge_labels = {(u, v): f"{kiyv_map.distances[u][v]:.1f}" for u, v in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("Graph")
        plt.axis("off")
        plt.savefig(Config.output_dir + f'{label}.png')
        plt.show()

    @staticmethod
    def draw_graph(graph, label="graph"):
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
        plt.savefig(Config.output_dir + f'{label}.png')
        plt.show()


    @staticmethod
    def draw_spanning_tree(graph: Graph, mst_edges, label="minimum_spanning_tree"):
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
        plt.savefig(Config.output_dir + f'{label}.png')
        plt.show()


    @classmethod
    def draw_strongly_connected_components(cls, scc_list, graph: Graph, label="strongly_connected_components"):
        for i, scc in enumerate(scc_list):
            scc_graph = nx.Graph()
            for node in scc:
                scc_graph.add_node(node)
            for u in scc:
                for v in scc:
                    if u != v and graph.distances[u][v] != np.inf:
                        scc_graph.add_edge(u, v)

            plt.figure(figsize=(8, 6))


            labels = {node: graph.get_label(node) for node in scc}
            nx.draw(scc_graph, with_labels=True, node_size=2000, labels=labels, node_color='lightblue', font_size=12, font_weight='bold')            
            plt.title(f"Strongly Connected Component {i+1}")
            plt.savefig(Config.output_dir + f'{label}_{i+1}.png')
            plt.show()
            
