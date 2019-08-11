import sys
import networkx as nx

def analyse_graph(G):
	no_of_connected_components = len(list(nx.connected_components(G)))
	print("Number of connected components : ", no_of_connected_components)#no of connected components
	max_degree = max(dict(G.degree()).values())
	print("Maximum degree : ", max_degree)#max degree
	no_of_nodes = len(G.nodes())
	total_degree = sum(dict(G.degree()).values())
	print("Average degree : ", total_degree/no_of_nodes)#avg degree
	total_clustering_coeff = sum(nx.clustering(G).values())
	print("Average clustering coefficient : ", total_clustering_coeff/no_of_nodes)#avg clustering coeff

if __name__ == '__main__':
	try:
		G = nx.read_edgelist(argv[1])
		analyse_graph(G)
	except FileNotFoundError:
		print("Check the file name you entered")
