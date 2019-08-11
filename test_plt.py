import networkx as nx
G = nx.read_edgelist('com-youtube.ungraph.txt')
try:
	diam = nx.diameter(G)
	print(diam)
except nx.NetworkXError:
	for C in nx.connected_component_subgraphs(G):
	    print(nx.diameter(C))
