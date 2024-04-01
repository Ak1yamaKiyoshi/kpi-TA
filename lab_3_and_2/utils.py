import random
from tqdm import tqdm
import timeit
from graph import Graph, GraphOperations
from typing import List

def random_init_nodes(size):
    nodes = []
    for i in range(size):
        nodes.append((i, f"Node {i}"))
    return nodes


def random_init_graph(nodes):
    num_nodes = len(nodes)
    graph = Graph(num_nodes)

    max_distance = 10
    max_flow = 400
    for u in range(num_nodes):
        for v in range(u + 1, num_nodes):
            distance = max_distance
            flow = max_flow
            graph.add_edge(u=u, v=v, distance=distance, flow=flow)
    return graph


class AvaivableOperations:
    dijkstra = "dijkstra"
    ford_fulkerson = "ford_fulkerson"
    dfs = "dfs"
    transpose = "transpose"
    mst = "mst"
    graph_coloring = "graph_coloring"
    algorythm_component_silnoji_zviyaznosty_po_shlyahah = "algorythm_component_silnoji_zviyaznosty_po_shlyahah."
    tarjan = "tarjan"

def benchmark(operations=[], max_size=50):
    bench_results = []
    population = 5
    sizes = [int(i * 1.5) for i in range(2, max_size)]
    for size in tqdm(sizes, desc="Benchmarking"):
        nodes = random_init_nodes(size)
        graph = random_init_graph(nodes)
        if AvaivableOperations.dijkstra in operations:
            bench_results.append({"operation": "dijkstra (O(n^2))", "time": 
                benchmark_operation(graph, 'dijkstra', population), "size": size})
        if AvaivableOperations.ford_fulkerson  in operations:
            bench_results.append({"operation": "ford_fulkerson (O(n^3))", "time": 
                benchmark_operation(graph, 'ford_fulkerson', population), "size": size})
        if AvaivableOperations.dfs in operations:
            bench_results.append({"operation": "dfs (O(n))", "time": 
                benchmark_operation(graph, 'dfs', population), "size": size})
        if AvaivableOperations.transpose in operations:
            bench_results.append({"operation": "transpose (O(n^2))", "time": 
                benchmark_operation(graph, 'transpose', population), "size": size})
        if AvaivableOperations.mst in operations:
            bench_results.append({"operation": "minimum_spanning_tree", "time": 
                benchmark_operation(graph, 'minimum_spanning_tree', population), "size": size})
        if AvaivableOperations.graph_coloring in operations:
            bench_results.append({"operation": "graph_coloring", "time": 
                benchmark_operation(graph, 'graph_coloring', population), "size": size})
        if AvaivableOperations.algorythm_component_silnoji_zviyaznosty_po_shlyahah in operations:
            bench_results.append({"operation": "algorythm_component_silnoji_zviyaznosty_po_shlyahah (O(n^2 log n))", "time":
                benchmark_operation(graph, 'algorythm_component_silnoji_zviyaznosty_po_shlyahah ', population), "size": size})
        if AvaivableOperations.tarjan in operations:
            bench_results.append({"operation": "tarjan (O(n^2 log n))", "time":
                benchmark_operation(graph, 'tarjan', population), "size": size})
    return bench_results


def benchmark_operation(graph: Graph, operation: str, iterations):
    time = 0.
    if operation == "dijkstra":
        time = timeit.timeit(lambda: GraphOperations.dijkstra(graph, 0), number=iterations)
    elif operation == "ford_fulkerson":
        time = timeit.timeit(lambda: GraphOperations.ford_fulkerson(graph, 0, graph.num_nodes - 1), number=iterations)
    elif operation == "minimum_spanning_tree":
        time = timeit.timeit(lambda: GraphOperations.minimum_spanning_tree(graph), number=iterations)
    elif operation == "graph_coloring":
        time = timeit.timeit(lambda: GraphOperations.graph_coloring(graph), number=iterations)
    elif operation == "algorythm_component_silnoji_zviyaznosty_po_shlyahah":
        time = timeit.timeit(lambda: GraphOperations.algorythm_component_silnoji_zviyaznosty_po_shlyahah(graph), number=iterations)
    elif operation == "tarjan":
        time = timeit.timeit(lambda: GraphOperations.tarjan_scc(graph), number=iterations)
    elif operation == "dfs":
        time = timeit.timeit(lambda: GraphOperations.dfs(graph, 0, [False] * graph.num_nodes, []), number=iterations)
    elif operation == "transpose":
        time = timeit.timeit(lambda: GraphOperations.transpose(graph), number=iterations)
        
    return time
