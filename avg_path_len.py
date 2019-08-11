import networkx as nx
G = nx.read_edgelist('com-youtube.ungraph.txt')
try:
	avg_path_len = nx.average_shortest_path_length(G)
	print(avg_path_len)
except nx.NetworkXError:
	for C in nx.connected_component_subgraphs(G):
	    print(nx.average_shortest_path_length(C))
