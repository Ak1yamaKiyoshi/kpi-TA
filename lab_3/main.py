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


kiyv_map = Graph(12)
kiyv_map.add_edge(0,  1, 1, 1)
kiyv_map.add_edge(1,  2, 1, 1)
kiyv_map.add_edge(2,  0, 1, 1)
kiyv_map.add_edge(3,  4, 1, 1)
kiyv_map.add_edge(4,  4, 1, 1)
kiyv_map.add_edge(5,  1, 1, 1)
kiyv_map.add_edge(6,  2, 1, 1)
kiyv_map.add_edge(7,  0, 1, 1)
kiyv_map.add_edge(8,  4, 1, 1)
kiyv_map.add_edge(9,  4, 1, 1)
kiyv_map.add_edge(10, 0, 1, 1)
kiyv_map.add_edge(11, 4, 1, 1)

kiyv_map.set_label(0, "Червоний університет")
kiyv_map.set_label(1, "Андріївська церква")
kiyv_map.set_label(2, "Михайлівський собор")
kiyv_map.set_label(3, "Золоті ворота")
kiyv_map.set_label(4, "Лядські ворота")
kiyv_map.set_label(5, "Фунікулер")
kiyv_map.set_label(6, "Київська політехніка")
kiyv_map.set_label(7, "Фонтан на Хрещатику")
kiyv_map.set_label(8, "Софія київська")
kiyv_map.set_label(9, "Національна філармонія")
kiyv_map.set_label(10, "Музей однієї вулиці")
kiyv_map.set_label(11, "Гуртожиток НТУУ КПІ")


GraphOperations.draw_graph(kiyv_map, "kiyv_map")

kosaraju = GraphOperations.kosaraju(kiyv_map)
GraphOperations.draw_strongly_connected_components(kosaraju, kiyv_map, "kosaraju")
print(f"Kosaraju's algorithm: {kosaraju}")

tarjan = GraphOperations.tarjan_scc(kiyv_map)
GraphOperations.draw_strongly_connected_components(tarjan, kiyv_map, "tarjan")
print(f"Tarjan's algorithm: {tarjan}")

mst_edges, _ = GraphOperations.minimum_spanning_tree(kiyv_map)
GraphOperations.draw_spanning_tree(kiyv_map, mst_edges)

max_flow = GraphOperations.ford_fulkerson(kiyv_map, 0, kiyv_map.num_nodes - 1)
print(f"Max flow: {max_flow}")

colors = GraphOperations.graph_coloring(kiyv_map)
color_map = [colors[node]
for node in range(kiyv_map.num_nodes)]
to_save = {"colors_map":color_map, "colors": colors, "needed_colors": len(set(color_map))}
print(f"Needed amount colors: {len(set(color_map))}")
with open(Config.output_dir + 'colors.txt', 'w') as f: f.write(str(to_save))

djkstra_results = GraphOperations.dijkstra(kiyv_map, 0)
print(f"Dijkstra results (distances to nodes from 0 node): {djkstra_results[0]}")


run_benchmark()