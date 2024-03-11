from pprint import pprint
from initial import kyiv_map
from Graph import GraphColoring
from colorama import Style, Fore, init
import warnings
warnings.filterwarnings("ignore")
init()



for edge in kyiv_map.edges:
    print(f"{edge.start.name} -> {edge.end.name}, Distance: {edge.distance} km, One-way: {edge.one_way}")
kyiv_map.draw()


#Є, 1 Відвідати всі вузли від
## Одного вузла до всіх інших (дейкстра)
node = "Гуртожиток НТУУ КПІ"
print(
    Fore.GREEN, f"Відвідати всі вузли від вузла {node}", Fore.RESET
)
pprint(kyiv_map.dijkstra(node))


#2 А -> В Максимальний потік 
## Алгоритм форда фаргелса
node = "Київська політехніка"
node1 = "Гуртожиток НТУУ КПІ"
print(   
    Fore.BLUE, f"Максимальний потік від {node} до {node1}",
    Fore.RESET, kyiv_map.ford_fulkerson(node, node1),
)

#Є, 3 Мінімальне кістякове дерево 
## Поєднати всі вершини між 
## собою, прибираючи зайві ребра
print(Fore.GREEN, "Мінімальне кістякове дерево. ", Fore.RESET)
mst_edges = kyiv_map.prim_minimum_spanning_tree("Київська політехніка")
for edge in mst_edges:
    if edge:
        print(edge.start.name, "->", edge.end.name, ":", edge.distance)
spanning_tree = kyiv_map.build_graph_from_edges(mst_edges)
spanning_tree.draw()


#Є, 4 Розфарбування графів 
## Кількість кольорів(?)
coloring = GraphColoring(kyiv_map)
color_map = coloring.greedy_coloring()
num_colors = len(set(color_map.values()))
print(Fore.GREEN, "Мінімальна кількість кольорів:", Fore.RESET, num_colors)
