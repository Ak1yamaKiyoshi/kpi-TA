import tkinter as tk
from tkinter import messagebox
from graph import Graph, GraphOperations
from utils import AvaivableOperations
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
]


kiyv_map = Graph(11)
kiyv_map.add_edge(u=0,  v=1, distance=2.0,   flow=400)
kiyv_map.add_edge(u=0,  v=2, distance=1.7,   flow=400)
kiyv_map.add_edge(u=0,  v=3, distance=0.9,   flow=400)
kiyv_map.add_edge(u=0,  v=5, distance=2.5,   flow=400)
kiyv_map.add_edge(u=0,  v=6, distance=5.0,   flow=400)
kiyv_map.add_edge(u=0,  v=7, distance=1.0,   flow=400)
kiyv_map.add_edge(u=0,  v=9, distance=2.5,   flow=400)
kiyv_map.add_edge(u=1,  v=2, distance=0.6,   flow=400)
kiyv_map.add_edge(u=1,  v=3, distance=1.3,   flow=400)
kiyv_map.add_edge(u=1,  v=7, distance=2.0,   flow=400)
kiyv_map.add_edge(u=1,  v=8, distance=0.95,  flow=400)
kiyv_map.add_edge(u=1,  v=10, distance=0.6,  flow=400)
kiyv_map.add_edge(u=2,  v=0, distance=1.7,   flow=400)
kiyv_map.add_edge(u=2,  v=3, distance=1.0,   flow=400)
kiyv_map.add_edge(u=3,  v=0, distance=0.9,   flow=400)
kiyv_map.add_edge(u=3,  v=1, distance=1.3,   flow=400)
kiyv_map.add_edge(u=3,  v=7, distance=1.0,   flow=400)
kiyv_map.add_edge(u=3,  v=3, distance=0.55,  flow=400)
kiyv_map.add_edge(u=4,  v=2, distance=0.5,   flow=400)
kiyv_map.add_edge(u=4,  v=7, distance=1.1,   flow=400)
kiyv_map.add_edge(u=5,  v=5, distance=0.75,  flow=400)
kiyv_map.add_edge(u=6,  v=0, distance=5.0,   flow=400)
kiyv_map.add_edge(u=7,  v=0, distance=1.0,   flow=400)
kiyv_map.add_edge(u=7,  v=1, distance=2.0,   flow=400)
kiyv_map.add_edge(u=7,  v=4, distance=1.1,   flow=400)
kiyv_map.add_edge(u=7,  v=8, distance=1.1,   flow=400)
kiyv_map.add_edge(u=8,  v=4, distance=0.75,  flow=400)
kiyv_map.add_edge(u=9,  v=0, distance=2.3,   flow=400)
kiyv_map.add_edge(u=9,  v=5, distance=0.75,  flow=400)
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
kiyv_map.set_pos(10, (400, 350))


try: os.mkdir(Config.output_dir)
except: pass    


def run_selected_algorithm():
    global kiyv_map
    start_node = int(selected_start_node.get())
    end_node = int(selected_end_node.get())
    if start_node == end_node:
        messagebox.showerror("Error", "Starting and ending nodes cannot be the same!")
        return

    run_algorithm(AvaivableOperations.ford_fulkerson, start_node, end_node)

def run_algorithm(algorithm, start_node, end_node):
    global kiyv_map
    if algorithm == AvaivableOperations.ford_fulkerson:
        max_flow, path = GraphOperations.ford_fulkerson(kiyv_map, start_node, end_node, return_path=True)


    print(f"Max flow: {max_flow}")
    messagebox.showinfo("Max Flow", f"Maximum Flow: {max_flow}")
    GraphOperations.draw_kiyv_map(kiyv_map, paths=path)

root = tk.Tk()
root.title("Algorithm Selection")

selected_algorithm = tk.StringVar()
selected_start_node = tk.StringVar()
selected_end_node = tk.StringVar()


tk.Label(root, text="Select Starting Node:").pack()

start_node_frame = tk.Frame(root)
start_node_frame.pack(side="left")

for node_id, node_name in nodes:
    tk.Radiobutton(start_node_frame, text=node_name, variable=selected_start_node, value=node_id).pack(anchor="w")

tk.Label(root, text="Select Ending Node:").pack()

end_node_frame = tk.Frame(root)
end_node_frame.pack(side="right")

for node_id, node_name in nodes:
    tk.Radiobutton(end_node_frame, text=node_name, variable=selected_end_node, value=node_id).pack(anchor="e")

tk.Button(root, text="Run Algorithm", command=run_selected_algorithm).pack()

root.mainloop()