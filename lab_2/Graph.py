from collections import deque
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
import networkx as nx
import heapq
import random
import timeit
import matplotlib.pyplot as plt



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
    
    
    def ford_fulkerson(self, start_node_name: str, end_node_name: str) -> float:
        start_node = self[start_node_name]
        end_node = self[end_node_name]

        if start_node is None or end_node is None:
            raise ValueError("Invalid start or end node name.")

        max_flow = 0

        while True:
            path_flow, path = self.bfs(start_node, end_node)

            if path_flow == 0:
                break

            max_flow += path_flow

            v = end_node
            print( v == start_node )
            while v != start_node:
                u = path[v]
                edge = next(e for e in self.edges if (e.start == u and e.end == v) or (e.end == u and e.start == v))
                if edge.start == u:
                    edge.flow += path_flow
                else:
                    edge.flow -= path_flow
                v = u
        
        return max_flow


    def bfs(self, start_node: Node, end_node: Node) -> Tuple[float, Dict[Node, Node]]:
        queue = deque([(start_node, 400)])
        path = {start_node: None}
        path_flow = 0

        while queue:
            u, flow = queue.popleft()

            for edge in self.edges:
                if edge.start == u:
                    v = edge.end
                    residual_capacity = edge.capacity - edge.flow
                elif edge.end == u:
                    v = edge.start
                    residual_capacity = edge.flow
                else:
                    continue

                if v not in path and residual_capacity > 0:
                    path[v] = u
                    new_flow = max(flow, residual_capacity)
                    if v == end_node:
                        path_flow = new_flow
                        break
                    
                    queue.append((v, new_flow))
        
        return path_flow , path


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
        color_map = {}
        for node in self.graph.nodes:
            used_colors = set()
            for neighbor in self.get_neighbors(node):
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])

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


def create_graph(n):
    graph = Graph()
    for i in range(n):
        graph.add_node(str(i))
    
    for i in range(n):
        for j in range(i+1, n):
            distance = random.randint(1, 10)
            graph.add_edge(graph[str(i)], graph[str(j)], distance)
            graph.add_edge(graph[str(j)], graph[str(i)], distance)
    
    start_node = graph[str(0)]
    return graph, start_node.name

def benchmark_dijkstra(n):
    graph, start_node_name = create_graph(n)
    stmt = f"graph.dijkstra('{start_node_name}')"
    setup = f"from __main__ import Graph, create_graph; graph, start_node_name = create_graph({n})"
    return timeit.timeit(stmt, setup=setup, number=10)

def benchmark_naive(n):
    distances = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    
    for i in range(n):
        for j in range(i+1, n):
            distance = random.randint(1, 10)
            distances[i][j] = distance
            distances[j][i] = distance
    
    stmt = """
for k in range(n):
    for i in range(n):
        for j in range(n):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
"""
    setup = f"n = {n}; distances = {distances}"
    return timeit.timeit(stmt, setup=setup, number=10)


if __name__ == "__main__":
    sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    dijkstra_times = []
    naive_times = []

    for size in sizes:
        print(f"Running for size {size}...")
        dijkstra_time = benchmark_dijkstra(size)
        naive_time = benchmark_naive(size)
        dijkstra_times.append(dijkstra_time)
        naive_times.append(naive_time)
        print(f"Dijkstra: {dijkstra_time:.6f} seconds, Naive: {naive_time:.6f} seconds")

    plt.plot(sizes, dijkstra_times, label='Dijkstra')
    plt.plot(sizes, naive_times, label='Naive')
    plt.xlabel('Graph Size')
    plt.ylabel('Time (seconds)')
    plt.title('Dijkstra vs O(n^2) Algorithm')
    plt.legend()
    plt.show()
