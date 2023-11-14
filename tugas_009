"""import numpy as np

adja_matrix = np.array ([[0,1,0,0,1],
                         [1,0,1,1,1],
                         [0,1,0,1,0],
                         [0,1,1,0,1],
                         [1,1,0,1,0]])

damping_factor = 0.85

num_pages = len(adja_matrix)
page_rank = np.ones(num_pages) / num_pages

num_iterations = 100

for i in range(num_iterations):
    new_page_rank = np.zeros(num_pages)
    for j in range (num_pages):
        linking_pages = [k for k in range (num_pages)if adja_matrix[k,j] == 1]
        for linking_page in linking_pages :
            new_page_rank [j] += page_rank[linking_page] / sum(adja_matrix[linking_page, :])
        new_page_rank[j] = damping_factor * new_page_rank[j] + (1 - damping_factor) / num_pages
    page_rank = new_page_rank

for page, rank in enumerate(page_rank):
    print(f"PR(page {page+1}) = {rank:.3f}")

import networkx as nx
import numpy as np

def CreatePageRank(aGraph):
    nodes_set = len(aGraph)
    M = nx.to_numpy_array(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    prob_outwards = np.array(1.0 / outwards)
    G = np.multiply(M, prob_outwards [:,np.newaxis])

    p = np.ones(nodes_set) / float(nodes_set)
    return G, p

myWeb = nx.DiGraph()
connections = [(1,2),(2,3),(3,4),(4,5),(5,6)]
myWeb.add_edges_from(connections)

G, p = CreatePageRank(myWeb)
print(G)

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adja_matrix = np.array ([[ 0,  1,  0,  0,  0,  0],
                         [ 0,  0,  1,  0,  0,  0],
                         [ 0,  0,  0,  1,  0,  0],
                         [ 0,  0,  0,  0,  1,  0],
                         [ 0,  0,  0,  0,  0,  1],
                         [ 0,  0,  0,  0,  0,  0]])

G = nx.DiGraph()

num_pages = len(adja_matrix)
G.add_nodes_from(range(num_pages))

for i in range (num_pages):
     for j in range (num_pages):
        if adja_matrix[i,j] == 1:
            G.add_edge(i,j)

pos = nx.spring_layout(G)
labels = {i: f"Page {i+1}" for i in range(num_pages)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000,node_color='grey', font_size=10,font_color='black',font_weight='bold',arrowsize=20)
plt.title("PageRank Example Graph")
plt.show()

import networkx as nx
import numpy as np

def CreatePageRank(aGraph):
    nodes_set = len(aGraph)
    M = nx.to_numpy_array(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    prob_outwards = np.array(1.0 / outwards)
    G = np.multiply(M, prob_outwards [:,np.newaxis])

    p = np.ones(nodes_set) / float(nodes_set)
    return G, p

myWeb = nx.DiGraph()
connections = [(1,2),(2,3),(3,4),(4,5),(5,1)]
myWeb.add_edges_from(connections)

G, p = CreatePageRank(myWeb)
print(G)

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adja_matrix = np.array ([[0, 1, 0, 0, 0],
                         [0, 0, 1, 0, 0],
                         [0, 0, 0, 1, 0],
                         [0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0]])

G = nx.DiGraph()

num_pages = len(adja_matrix)
G.add_nodes_from(range(num_pages))

for i in range (num_pages):
     for j in range (num_pages):
        if adja_matrix[i,j] == 1:
            G.add_edge(i,j)

pos = nx.spring_layout(G)
labels = {i: f"Page {i+1}" for i in range(num_pages)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000,node_color='grey', font_size=10,font_color='black',font_weight='bold',arrowsize=20)
plt.title("PageRank Example Graph")
plt.show()

import networkx as nx
import numpy as np

def CreatePageRank(aGraph):
    nodes_set = len(aGraph)
    M = nx.to_numpy_array(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    prob_outwards = np.array(1.0 / outwards)
    G = np.multiply(M, prob_outwards [:,np.newaxis])

    p = np.ones(nodes_set) / float(nodes_set)
    return G, p

myWeb = nx.DiGraph()
connections = [(1,2),(2,3),(2,1),(3,4),(3,2),(4,3)]
myWeb.add_edges_from(connections)

G, p = CreatePageRank(myWeb)
print(G)

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adja_matrix = np.array ([[0, 1, 0, 0],
                         [1, 0, 1, 0],
                         [0, 1, 0, 1],
                         [0, 0, 1, 0]])

G = nx.DiGraph()

num_pages = len(adja_matrix)
G.add_nodes_from(range(num_pages))

for i in range (num_pages):
     for j in range (num_pages):
        if adja_matrix[i,j] == 1:
            G.add_edge(i,j)

pos = nx.spring_layout(G)
labels = {i: f"Page {i+1}" for i in range(num_pages)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000,node_color='grey', font_size=10,font_color='black',font_weight='bold',arrowsize=20)
plt.title("PageRank Example Graph")
plt.show()

import networkx as nx
import numpy as np

def CreatePageRank(aGraph):
    nodes_set = len(aGraph)
    M = nx.to_numpy_array(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    prob_outwards = np.array(1.0 / outwards)
    G = np.multiply(M,prob_outward s [:,np.newaxis])

    p = np.ones(nodes_set) / float(nodes_set)
    return G, p

myWeb = nx.DiGraph()
connections = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1)]
myWeb.add_edges_from(connections)

G, p = CreatePageRank(myWeb)
print(G)

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adja_matrix = np.array ([[0, 1, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0],
                         [0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0]])

G = nx.DiGraph()

num_pages = len(adja_matrix)
G.add_nodes_from(range(num_pages))

for i in range (num_pages):
     for j in range (num_pages):
        if adja_matrix[i,j] == 1:
            G.add_edge(i,j)

pos = nx.spring_layout(G)
labels = {i: f"Page {i+1}" for i in range(num_pages)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000,node_color='grey', font_size=10,font_color='black',font_weight='bold',arrowsize=20)
plt.title("PageRank Example Graph")
plt.show()

import networkx as nx
import numpy as np

def CreatePageRank(aGraph):
    nodes_set = len(aGraph)
    M = nx.to_numpy_array(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    prob_outwards = np.array(1.0 / outwards)
    G = np.multiply(M,prob_outwards [:,np.newaxis])

    p = np.ones(nodes_set) / float(nodes_set)
    return G, p

myWeb = nx.DiGraph()
connections = [(1,2),(2,3),(2,1),(3,2),(3,4),(4,1),(4,3)]
myWeb.add_edges_from(connections)

G, p = CreatePageRank(myWeb)
print(G)

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adja_matrix = np.array ([[0, 1, 0, 0],
                         [1, 0, 1, 0],
                         [0, 1, 0, 1],
                         [1, 0, 1, 0]])

G = nx.DiGraph()

num_pages = len(adja_matrix)
G.add_nodes_from(range(num_pages))

for i in range (num_pages):
     for j in range (num_pages):
        if adja_matrix[i,j] == 1:
            G.add_edge(i,j)

pos = nx.spring_layout(G)
labels = {i: f"Page {i+1}" for i in range(num_pages)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000,node_color='grey', font_size=10,font_color='black',font_weight='bold',arrowsize=20)
plt.title("PageRank Example Graph")
plt.show()

import networkx as nx
import numpy as np

def CreatePageRank(aGraph):
    nodes_set = len(aGraph)
    M = nx.to_numpy_array(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    prob_outwards = np.array(1.0 / outwards)
    G = np.multiply(M, prob_outwards [:,np.newaxis])

    p = np.ones(nodes_set) / float(nodes_set)
    return G, p

myWeb = nx.DiGraph()
connections = [(1,2),(2,3),(3,4),(4,1),(4,5),(5,1)]
myWeb.add_edges_from(connections)

G, p = CreatePageRank(myWeb)
print(G)

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adja_matrix = np.array ([[ 0,  1,  0,  0,  0],
                         [ 0,  0,  1,  0,  0],
                         [ 0,  0,  0,  1,  0],
                         [ 1,  0,  0,  0,  1],
                         [ 1,  0,  0,  0,  0]])

G = nx.DiGraph()

num_pages = len(adja_matrix)
G.add_nodes_from(range(num_pages))

for i in range (num_pages):
     for j in range (num_pages):
        if adja_matrix[i,j] == 1:
            G.add_edge(i,j)

pos = nx.spring_layout(G)
labels = {i: f"Page {i+1}" for i in range(num_pages)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000,node_color='grey', font_size=10,font_color='black',font_weight='bold',arrowsize=20)
plt.title("PageRank Example Graph")
plt.show()

import networkx as nx
import numpy as np

def CreatePageRank(aGraph):
    nodes_set = len(aGraph)
    M = nx.to_numpy_array(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    prob_outwards = np.array(1.0 / outwards)
    G = np.multiply(M, prob_outwards [:,np.newaxis])

    p = np.ones(nodes_set) / float(nodes_set)
    return G, p

myWeb = nx.DiGraph()
connections = [(1,2),(2,3),(2,1),(3,1),(3,3)]
myWeb.add_edges_from(connections)

G, p = CreatePageRank(myWeb)
print(G)

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adja_matrix = np.array ([[0, 1, 0],
                         [1, 0, 1],
                         [1, 0, 1]])

G = nx.DiGraph()

num_pages = len(adja_matrix)
G.add_nodes_from(range(num_pages))

for i in range (num_pages):
     for j in range (num_pages):
        if adja_matrix[i,j] == 1:
            G.add_edge(i,j)

pos = nx.spring_layout(G)
labels = {i: f"Page {i+1}" for i in range(num_pages)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size=1000,node_color='grey', font_size=10,font_color='black',font_weight='bold',arrowsize=20)
plt.title("PageRank Example Graph")
plt.show()
