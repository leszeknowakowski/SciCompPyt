import random
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
num_nodes = 7
nodes = range(1, num_nodes + 1)
G.add_nodes_from(nodes)
num_edges = 15

edges = []

while len(edges) < num_edges:
    x = random.randint(1, num_nodes)
    y = random.randint(1, num_nodes)
    if x != y:
        edges.append((x, y))



G.add_edges_from(edges)
def trivial_node_coloring(graph):
    """Trivial node coloring."""
    counter = 0
    for node in graph.nodes:
        graph.nodes[node]['color'] = counter
        counter += 1

    colors = [graph.nodes[node]['color'] for node in graph.nodes]
    return colors


col = trivial_node_coloring(G)

nx.draw(G, with_labels=True, node_color=col, cmap='rainbow')
plt.show()