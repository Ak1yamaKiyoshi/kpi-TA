from Graph import  Node, Edge, Graph
import networkx as nx
from typing import List, Tuple
from initial import kyiv_map, places

# Display the graph
for edge in kyiv_map.edges:
    print(f" ALL EDGES")
    print(f"{edge.start.name} -> {edge.end.name}, Distance: {edge.distance} km, One-way: {edge.one_way}")

kyiv_map.draw()