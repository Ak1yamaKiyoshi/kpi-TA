from graph import Graph, GraphOperations
from utils import random_init_graph
from benchmark import run_benchmark
from config import Config
import os


nodes = [
    (0, "Червоний університет"),
    (1, "Андріївська церква"),
    (2, "Михайлівський собор"),
    (3, "Золоті ворота"),
    (4, "Лядські ворота"),
    (5, "Фунікулер"),
    (6, "Київська політехніка"),
    (7, "Фонтан на Хрещатику"),
    (8, "Софія київська"),
    (9, "Національна філармонія"),
    (10, "Музей однієї вулиці"),
    (11, "Гуртожиток НТУУ КПІ")
]

try: os.mkdir(Config.output_dir)
except: pass

# Init map
kiyv_map = random_init_graph(nodes)
GraphOperations.draw_graph(kiyv_map)

# Djkstra 
djkstra_results = GraphOperations.dijkstra(kiyv_map, 0)
print(f"Dijkstra results: {djkstra_results}")

# Minimum spanning tree 
mst_edges, _ = kiyv_map.minimum_spanning_tree()
GraphOperations.draw_spanning_tree(kiyv_map, mst_edges)

# Coloring 
colors = GraphOperations.graph_coloring(kiyv_map)
color_map = [colors[node] for node in range(kiyv_map.num_nodes)]
to_save = {"colors_map": color_map, "colors": colors, "needed_colors": len(set(color_map))}
print(f"Needed amount colors: {len(set(color_map))}")
with open(Config.output_dir + 'colors.txt', 'w') as f: f.write(str(to_save))

# Max flow using ford fulkerson
max_flow = GraphOperations.ford_fulkerson(kiyv_map, 0, kiyv_map.num_nodes - 1)
print(f"Max flow: {max_flow}")

# Benchmark 
run_benchmark()

# Done
print(f"Results saved in {Config.output_dir} directory.")
print("""Lab work was done by: 
- Kolosov Ihor
- Pedko Mykyta
- ???? Vladyslav""")