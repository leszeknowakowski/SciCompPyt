import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Importing data.
with open("C:\\Users\\lesze\\Downloads\\tokyo-metro.json") as infile:
    D = json.load(infile)

print(list(D))   # metro lines (keys)
# ['C', 'G', 'F', 'H', 'M', 'N', 'T', 'Y', 'Z']

print(D['C'])   # line info (values are dicts)
# {'color': '#149848',
# 'transfers': [['C3', 'F15'], ['C4', 'Z2'], ...],
# 'travel_times': [['C1', 'C2', 2], ['C2', 'C3', 2], ...]}

# Creating the metro graph.
G = nx.Graph()
for line in D.values():
    G.add_weighted_edges_from(line["travel_times"])
    G.add_edges_from(line["transfers"])

# Edges for transfers do not have weights.
# We add the additional attribute (bool) for all edges.
for (node1, node2) in G.edges():
    G[node1][node2]['transfer'] = ("weight" not in G[node1][node2])

# We add 5 minutes for transfer.
for (node1, node2) in G.edges():
    if G[node1][node2]['transfer']:
        G[node1][node2]['weight'] = 5

# Colors for all nodes from the same metro line.
# node[0] gives the metro line.
colors = [D[node[0].upper()]["color"] for node in G.nodes()]
print(colors)

nx.draw(G, with_labels=True, node_color=colors)
plt.show()