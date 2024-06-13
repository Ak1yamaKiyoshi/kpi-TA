from graph import Graph, GraphOperations
from utils import random_init_graph, AvaivableOperations
from benchmark import run_benchmark
from config import Config
import os
import numpy as np
import tkinter as tk
from tkinter import ttk
from graph import Graph, GraphOperations
from utils import AvaivableOperations
from benchmark import run_benchmark


def run_algorithm():
    selected_algorithm = algorithm_combo.get()
    if selected_algorithm == "algorythm_component_silnoji_zviyaznosty_po_shlyahah":
        result_label.config(text=f"algorythm_component_silnoji_zviyaznosty_po_shlyahah algorithm: {GraphOperations.algorythm_component_silnoji_zviyaznosty_po_shlyahah(kiyv_map)}")
        scc = GraphOperations.algorythm_component_silnoji_zviyaznosty_po_shlyahah(kiyv_map)
        print(scc)
        GraphOperations.draw_kiyv_map(scc=scc, kiyv_map=kiyv_map, label="algorythm_component_silnoji_zviyaznosty_po_shlyahah")
    elif selected_algorithm == "Tarjan":
        result_label.config(text=f"Tarjan's algorithm: {GraphOperations.tarjan_scc(kiyv_map)}")
        scc = GraphOperations.tarjan_scc(kiyv_map)
        print(scc)
        GraphOperations.draw_kiyv_map(scc=scc, kiyv_map=kiyv_map, label="tarjan")
    else:
        result_label.config(text="Invalid algorithm selection")


nodes = [
    (1+0, "Червоний університет"),
    (1+1, "Андріївська церква"),
    (1+2, "Михайлівський собор"),
    (1+3, "Золоті ворота"),
    (1+4, "Лядські ворота"),
    (1+5, "Фунікулер"),
    (1+6, "Київська політехніка"),
    (1+7, "Фонтан на Хрещатику"),
    (1+8, "Софія київська"),
    (1+9, "Національна філармонія"),
    (1+10, "Музей однієї вулиці"),
]


try: os.mkdir(Config.output_dir)
except: pass


kiyv_map = Graph(11)
kiyv_map.add_edge(u=0, v=6, distance=5.0,   flow=400)
kiyv_map.add_edge(u=0, v=7, distance=1.0,   flow=400)
kiyv_map.add_edge(u=0, v=9, distance=2.5,   flow=400)

kiyv_map.add_edge(u=1, v=2, distance=0.6,   flow=400)
kiyv_map.add_edge(u=1, v=3, distance=1.3,   flow=400)
kiyv_map.add_edge(u=1, v=7, distance=2.0,   flow=400)
kiyv_map.add_edge(u=1, v=8, distance=0.95,  flow=400)
kiyv_map.add_edge(u=1, v=10, distance=0.6,  flow=400)
kiyv_map.add_edge(u=2, v=0, distance=1.7,   flow=400)
kiyv_map.add_edge(u=2, v=3, distance=1.0,   flow=400)
kiyv_map.add_edge(u=3, v=0, distance=0.9,   flow=400)
kiyv_map.add_edge(u=3, v=1, distance=1.3,   flow=400)
kiyv_map.add_edge(u=3, v=7, distance=1.0,   flow=400)
kiyv_map.add_edge(u=3, v=3, distance=0.55,  flow=400)
kiyv_map.add_edge(u=4, v=2, distance=0.5,   flow=400)
kiyv_map.add_edge(u=4, v=7, distance=1.1,   flow=400)
kiyv_map.add_edge(u=5, v=5, distance=0.75,  flow=400)
kiyv_map.add_edge(u=6, v=0, distance=5.0,   flow=400)
kiyv_map.add_edge(u=7, v=0, distance=1.0,   flow=400)
kiyv_map.add_edge(u=7, v=1, distance=2.0,   flow=400)
kiyv_map.add_edge(u=7, v=4, distance=1.1,   flow=400)
kiyv_map.add_edge(u=7, v=8, distance=1.1,   flow=400)
kiyv_map.add_edge(u=8, v=4, distance=0.75,  flow=400)
kiyv_map.add_edge(u=9, v=0, distance=2.3,   flow=400)
kiyv_map.add_edge(u=9, v=5, distance=0.75,  flow=400)
kiyv_map.add_edge(u=10, v=1, distance=0.6,  flow=400)
kiyv_map.add_edge(u=10, v=5, distance=0.8,  flow=400)


kiyv_map.set_label(0, "Червоний\nуніверситет")
kiyv_map.set_pos(0, (200, 300))
kiyv_map.set_label(1, "Андріївська\nцерква")
kiyv_map.set_pos(1, (200, 100))
kiyv_map.set_label(2, "Михайлівський\nсобор")
kiyv_map.set_pos(2, (500, 300))
kiyv_map.set_label(3, "Золоті\nворота")
kiyv_map.set_pos(3, (650, 100))
kiyv_map.set_label(4, "Лядські\nворота")
kiyv_map.set_pos(4, (700, 500))
kiyv_map.set_label(5, "Фунікулер")
kiyv_map.set_pos(5, (200, 500))
kiyv_map.set_label(6, "Київська\nполітехніка")
kiyv_map.set_pos(6, (100, 320))
kiyv_map.set_label(7, "Фонтан на\nХрещатику")
kiyv_map.set_pos(7, (800, 200))
kiyv_map.set_label(8, "Софія\nкиївська")
kiyv_map.set_pos(8, (800, 300))
kiyv_map.set_label(9, "Національна\nфілармонія")
kiyv_map.set_pos(9, (500, 600))
kiyv_map.set_label(10, "Музей однієї\nвулиці")
kiyv_map.set_pos(10, (400, 350)), 


root = tk.Tk()
root.title("Algorithm Selection")


algorithm_label = ttk.Label(root, text="Select Algorithm:")
algorithm_label.pack(pady=10)
algorithm_combo = ttk.Combobox(root, values=["algorythm_component_silnoji_zviyaznosty_po_shlyahah", "Tarjan"])
algorithm_combo.pack()

run_button = ttk.Button(root, text="Run Algorithm", command=run_algorithm)
run_button.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()

run_benchmark([
    AvaivableOperations.dfs, # O(n^(V+E))
    AvaivableOperations.ford_fulkerson, #(O(nlog(n^2)))
    AvaivableOperations.algorythm_component_silnoji_zviyaznosty_po_shlyahah,
    AvaivableOperations.tarjan,
    AvaivableOperations.transpose, # O(n^3)
    
], "lab3")