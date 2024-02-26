from initial import kyiv_map
from Graph import GraphColoring

# Display the graph
for edge in kyiv_map.edges:
    print(f" ALL EDGES")
    print(f"{edge.start.name} -> {edge.end.name}, Distance: {edge.distance} km, One-way: {edge.one_way}")

kyiv_map.draw()


#1 Відвідати всі вузли від
## Одного вузла до всіх інших (дейкстра)
from pprint import pprint
pprint(
    kyiv_map.dijkstra("Гуртожиток НТУУ КПІ")
)

#2 А -> В Максимальний пот  ік 
## Алгоритм форда фаргелса
#! Не працює 
pprint(   
    kyiv_map.ford_fulkerson("Київська політехніка", "Гуртожиток НТУУ КПІ")
)


#3 Мінімальне кістякове дерево 
## Поєднати всі вершини між 
## собою, прибираючи зайві ребра
mst_edges = kyiv_map.prim_minimum_spanning_tree("Київська політехніка")
for edge in mst_edges:
    if edge:
        print(edge.start.name, "->", edge.end.name, ":", edge.distance)
spanning_tree = kyiv_map.build_graph_from_edges(mst_edges)
spanning_tree.draw()

#4 Розфарбування графів 
## Кількість кольорів(?)
coloring = GraphColoring(kyiv_map)
color_map = coloring.greedy_coloring()
num_colors = len(set(color_map.values()))
print("Minimum number of colors required:", num_colors)
