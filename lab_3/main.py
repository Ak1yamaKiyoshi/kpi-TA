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

kiyv_map = Graph(5)
kiyv_map.add_edge(0, 1, 1, 1)
kiyv_map.add_edge(1, 2, 1, 1)
kiyv_map.add_edge(2, 0, 1, 1)
kiyv_map.add_edge(3, 4, 1, 1)
kiyv_map.add_edge(4, 4, 1, 1)
kiyv_map.set_label(0, "Червоний університет")
kiyv_map.set_label(1, "Андріївська церква")
kiyv_map.set_label(2, "Михайлівський собор")
kiyv_map.set_label(3, "Золоті ворота")
kiyv_map.set_label(4, "Лядські ворота")


GraphOperations.draw_graph(kiyv_map, "kiyv_map")

kosaraju = GraphOperations.kosaraju(kiyv_map)
GraphOperations.draw_strongly_connected_components(kosaraju, kiyv_map, "kosaraju")
print(f"Kosaraju's algorithm: {kosaraju}")

tarjan = GraphOperations.tarjan_scc(kiyv_map)
GraphOperations.draw_strongly_connected_components(tarjan, kiyv_map, "tarjan")
print(f"Tarjan's algorithm: {tarjan}")

run_benchmark()