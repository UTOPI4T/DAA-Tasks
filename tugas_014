# Latihan 1
vertices = range(1, 10)
edges = [(1, 2), (1, 7), (2, 3), (2, 6), (3, 4), (3, 6), (5, 6), (6, 7), (7, 8), (7, 9), (8, 9), (7, 10)]

G = nx.Graph()

G.add_nodes_from(vertices)
G.add_edges_from(edges)
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist=[1, 4, 5, 7, 10], label=True, node_color='r', node_size=1300, edgecolors='black', linewidths=2)
nx.draw_networkx_nodes(G, pos, nodelist=[2, 3, 6, 8, 9], label=True, node_color='g', node_size=1300, edgecolors='black', linewidths=2)
nx.draw_networkx_edges(G, pos, edges, width=2, alpha=1, edge_color='black')

labels = {}
labels[1] = r'1 F'
labels[2] = r'2 NF'
labels[3] = r'3 NF'
labels[4] = r'4 F'
labels[5] = r'5 F'
labels[6] = r'6 NF'
labels[7] = r'7 F'
labels[8] = r'8 NF'
labels[9] = r'9 NF'
labels[10] = r'10 F'

nx.draw_networkx_labels(G, pos, labels, font_size=10)

plt.show()
#_______________________________________________________________________________________
# Latihan 2
vertices = range(1, 15)
edges = [(7,4),(7,5),(7,8),(4,6),(6,9),(4,5),(5,3),(5,9),(5,8),(3,1),(3,2),(3,12),(3,11),(3,10),(1,2),(2,12),(12,13),(12,11),(11,10)]

G = nx.Graph()

G.add_nodes_from(vertices)
G.add_edges_from(edges)
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist=[1, 2, 3, 10, 11, 12], label=True, node_color='r', node_size=1000, edgecolors='black', linewidths=2)
nx.draw_networkx_nodes(G, pos, nodelist=[4, 5, 6, 7, 8, 9, 13], label=True, node_color='g', node_size= 1000, edgecolors='black', linewidths=2)
nx.draw_networkx_edges(G, pos, edges, width=2, alpha=1, edge_color='black')

labels = {}
labels[1] = r'1 F'
labels[2] = r'2 F'
labels[3] = r'3 F'
labels[4] = r'4 NF'
labels[5] = r'5 NF'
labels[6] = r'6 NF'
labels[7] = r'7 NF'
labels[8] = r'8 NF'
labels[9] = r'9 NF'
labels[10] = r'10 F'
labels[11] = r'11 F'
labels[12] = r'12 F'
labels[13] = r'13 NF'

nx.draw_networkx_labels(G, pos, labels, font_size=10)

plt.show()

