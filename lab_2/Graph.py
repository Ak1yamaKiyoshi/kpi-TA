from collections import deque
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
import networkx as nx
import heapq


class Node:
    def __init__(self, name):
        self.name = name
        self.distance = float('inf')
        self.visited = False
        self.previous: Optional[Node] = None

    def __lt__(self, other):
        return self.distance < other.distance

class Edge:
    def __init__(self, start: Node, end: Node, distance: float = None, one_way=False):
        self.start: Node = start
        self.end: Node = end
        self.distance: float = distance
        self.capacity = distance
        self.one_way: bool = one_way
        self.flow = 400

class Graph:
    def __init__(self):
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []

    def add_node(self, name: str):
        self.nodes.append(Node(name))

    def add_edge(self, start: Node, end: Node, distance=None, one_way=False):
        self.edges.append(Edge(start, end, distance, one_way))

    def __getitem__(self, key: str) -> Optional[Node]:
        results = [el for el in self.nodes if el.name == key]
        if len(results) > 0:
            return results[0]
        else:
            return None

    def dijkstra(self, start_node_name: str) -> Dict[str, Tuple[float, Optional[str]]]:
        start_node = self[start_node_name]
        start_node.distance = 0
        unvisited_nodes = [(node.distance, node) for node in self.nodes]
        heapq.heapify(unvisited_nodes)

        while unvisited_nodes:
            current_distance, current_node = heapq.heappop(unvisited_nodes)
            current_node.visited = True

            for edge in self.edges:
                if edge.start == current_node:
                    neighbor = edge.end
                elif not edge.one_way and edge.end == current_node:
                    neighbor = edge.start
                else:
                    continue

                if not neighbor.visited:
                    new_distance = current_distance + edge.distance
                    if new_distance < neighbor.distance:
                        neighbor.distance = new_distance
                        neighbor.previous = current_node
                        heapq.heappush(unvisited_nodes, (new_distance, neighbor))

        shortest_paths = {}
        for node in self.nodes:
            if node.distance == float('inf'):
                shortest_paths[node.name] = (float('inf'), None)
            else:
                shortest_paths[node.name] = (node.distance, node.previous.name if node.previous else None)

        return shortest_paths

    def bfs(self, source, sink):
        visited = {node: False for node in self.nodes}
        queue = deque([source])
        visited[source] = True
        parent = {source: None}

        while queue:
            u = queue.popleft()
            for edge in self.edges:  # Iterate directly over the edge list
                if edge.start == u and not visited[edge.end] and edge.capacity > edge.flow:
                    queue.append(edge.end)
                    visited[edge.end] = True
                    parent[edge.end] = u

        print(visited)
        return parent if edge.end == sink else None

    def ford_fulkerson(self, source, sink):
        parent = self.bfs(source, sink)
        while parent:
            path_flow = min(edge.capacity - edge.flow for edge in self.edges if edge.start == parent[v] and v != source)
            for edge in self.edges:
                if edge.start == parent[v] and v != source:
                    edge.flow += path_flow
                    self.edges[self.edges.index(edge) + 1].flow -= path_flow
                elif edge.end == parent[v] and v != sink: 
                    edge.flow -= path_flow
                    self.edges[self.edges.index(edge) - 1].flow += path_flow
                v = edge.end
            parent = self.bfs(source, sink)

        return sum(edge.flow for edge in self.edges if edge.start == source)


    def prim_minimum_spanning_tree(self, start_node_name: str) -> List[Edge]:
        start_node = self[start_node_name]
        start_node.distance = 0
        unvisited_nodes = [(node.distance, node) for node in self.nodes]
        heapq.heapify(unvisited_nodes)
        mst_edges = []

        while unvisited_nodes:
            current_distance, current_node = heapq.heappop(unvisited_nodes)
            current_node.visited = True

            if current_node.previous is not None:
                mst_edges.append(Edge(current_node.previous, current_node, current_distance))

            for edge in self.edges:
                if edge.start == current_node and not edge.end.visited:
                    if edge.distance < edge.end.distance:
                        edge.end.distance = edge.distance
                        edge.end.previous = current_node
                        heapq.heappush(unvisited_nodes, (edge.distance, edge.end))
                elif edge.end == current_node and not edge.start.visited:
                    if edge.distance < edge.start.distance:
                        edge.start.distance = edge.distance
                        edge.start.previous = current_node
                        heapq.heappush(unvisited_nodes, (edge.distance, edge.start))

        return mst_edges

    def build_graph_from_edges(self, mst_edges: List[Edge]):
        new_graph = Graph()
        node_names = set()
        
        # Add nodes and collect node names
        for edge in mst_edges:
            node_names.add(edge.start.name)
            node_names.add(edge.end.name)
            
        for name in node_names:
            new_graph.add_node(name)
        
        # Add edges to the new graph
        for edge in mst_edges:
            start_node = new_graph[edge.start.name]
            end_node = new_graph[edge.end.name]
            new_graph.add_edge(start_node, end_node, edge.distance)
        
        return new_graph

    def draw(self):
        G = nx.Graph()

        for node in self.nodes:
            G.add_node(node.name)

        for edge in self.edges:
            G.add_edge(edge.start.name, edge.end.name, weight=edge.distance)

        node_positions = nx.spring_layout(G, iterations=90, k=100)

        nx.draw_networkx_nodes(G, node_positions, node_size=400, node_color=(.123, .3, .5))
        nx.draw_networkx_edges(G, node_positions, width=1, alpha=1, edge_color='gray')

        edge_labels = {(edge.start.name, edge.end.name): f"{edge.distance} km" for edge in self.edges}
        nx.draw_networkx_edge_labels(G, node_positions, edge_labels=edge_labels, font_color='red', font_size=7)

        node_labels = {node.name: node.name for node in self.nodes}
        nx.draw_networkx_labels(G, node_positions, labels=node_labels, font_size=8)

        plt.title('Connections between Places in Kyiv')
        plt.axis('off')
        plt.show()


class GraphColoring:
    def __init__(self, graph):
        self.graph = graph

    def greedy_coloring(self):
        color_map = {}  # To store the color assigned to each node
        for node in self.graph.nodes:
            used_colors = set()  # Set to store colors used by neighboring nodes
            for neighbor in self.get_neighbors(node):
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])
            # Find the first available color
            for color in range(len(self.graph.nodes)):
                if color not in used_colors:
                    color_map[node] = color
                    break
        return color_map

    def get_neighbors(self, node):
        neighbors = set()
        for edge in self.graph.edges:
            if edge.start == node:
                neighbors.add(edge.end)
            elif not edge.one_way and edge.end == node:
                neighbors.add(edge.start)
        return neighbors