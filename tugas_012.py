Pertemuan 12 (asynchronous) :
import networkx as nx
import matplotlib.pyplot as plt

# Fungsi untuk menggambar graf
def draw_graph(G, pos, title):
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
    plt.title(title)
    plt.show()

# Buat objek graf terarah
G = nx.DiGraph()

# Tambahkan simpul (nodes)
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")


G.add_nodes_from(["E", "F", "G", "H",])
# Tambahkan tepi (edges)
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "D")
G.add_edge("B", "E")

G.add_edges_from([("E", "F"), ("F", "G"), ("G", "H")])

# Gambarkan graf
pos = nx.spring_layout(G)  # Tentukan posisi simpul
draw_graph(G, pos, "Original Graph")

# Lakukan DFS traversal
dfs_edges = list(nx.dfs_edges(G, source="A"))

# Gambarkan graf setelah DFS
draw_graph(G, pos, "Graph After DFS Traversal")

print("DFS Edges:", dfs_edges)

#______________________________________________________________

import networkx as nx
import matplotlib.pyplot as plt

# Fungsi untuk menggambar graf
def draw_graph(G, pos, title):
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
    plt.title(title)
    plt.show()

# Buat objek graf terarah
G = nx.DiGraph()

# Tambahkan simpul (nodes)
nodes = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(nodes)

# Tambahkan tepi (edges)
edges = [("A", "B"), ("B", "C"), ("C", "F"), ("B", "D"), ("D", "E"), ("E", "F")]
G.add_edges_from(edges)

# Gambarkan graf
pos = nx.spring_layout(G)  # Tentukan posisi simpul
draw_graph(G, pos, "Original Graph")

# Periksa apakah ada jalur dari "A" ke "F"
source = "A"
target = "F"
if nx.has_path(G, source=source, target=target):
    # Dapatkan jalur terpendek dari "A" ke "F"
    shortest_path = nx.shortest_path(G, source=source, target=target)
    print("Shortest Path from {} to {}: {}".format(source, target, shortest_path))
else:
    print("No path from {} to {}.".format(source, target))

#______________________________________________________________
