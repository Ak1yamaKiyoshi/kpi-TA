import random
from tqdm import tqdm
import timeit
from graph import Graph, GraphOperations


def random_init_nodes(size):
    nodes = []
    for i in range(size):
        nodes.append((i, f"Node {i}"))
    return nodes


def random_init_graph(nodes):
    graph = Graph(len(nodes))
    for node in nodes: graph.set_label(node[0], node[1])

    max_distance = 10
    max_flow = 400

    for _ in range(50):
        u = random.randint(0, len(nodes) - 1)
        v = random.randint(0, len(nodes) - 1)

        while u == v:
            v = random.randint(0, len(nodes) - 1)

        distance = random.randint(1, max_distance)
        flow = random.randint(1, max_flow)

        graph.add_edge(u=u, v=v, distance=distance, flow=flow)
    return graph


def benchmark(max_size=210):
    bench_results = []
    population = 7
    sizes = [int(i * 1.5) for i in range(2, max_size)]
    for size in tqdm(sizes, desc="Benchmarking"):
        nodes = random_init_nodes(size)
        graph = random_init_graph(nodes)
        bench_results.append({"operation": "dijkstra", "time": 
            benchmark_operation(graph, 'dijkstra', population), "size": size})
        bench_results.append({"operation": "ford_fulkerson", "time": 
            benchmark_operation(graph, 'ford_fulkerson', population), "size": size})
        bench_results.append({"operation": "minimum_spanning_tree", "time": 
            benchmark_operation(graph, 'minimum_spanning_tree', population), "size": size})
        bench_results.append({"operation": "graph_coloring", "time": 
            benchmark_operation(graph, 'graph_coloring', population), "size": size})
        bench_results.append({"operation": "kosaraju", "time": 
            benchmark_operation(graph, 'kosaraju', population), "size": size})
        bench_results.append({"operation": "tarjan", "time":
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
    elif operation == "kosaraju":
        time = timeit.timeit(lambda: GraphOperations.kosaraju(graph), number=iterations)
    elif operation == "tarjan":
        time = timeit.timeit(lambda: GraphOperations.tarjan_scc(graph), number=iterations)
    return time
