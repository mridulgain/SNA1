import sys
import networkx as nx
import matplotlib.pyplot as plt
def degree_distribution(g):
	dd = {}
	for n in g.nodes():
		deg = g.degree(n)
		if deg  not in dd:
			dd[deg] = 0
		dd[deg] += 1
	deg_count = sorted(dd.items ())
	fig = plt.figure ()
	ax = fig.add_subplot (111)
	k = [deg for (deg,count) in deg_count]
	no_of_nodes = len(g.nodes())
	pk = [count/no_of_nodes for (deg, count) in deg_count]
	ax.plot(k, pk)
	plt.title("Degree  Distribution")
	#fig.savefig("degree_distribution.png")
	plt.show()

def analyse_graph(G):
	# connected component count
	deg_list = dict(G.degree()).values()
	no_of_connected_components = len(list(nx.connected_components(G)))
	print("Number of connected components : ", no_of_connected_components)#no of connected components
	# max degree
	max_degree = max(deg_list)
	print("Maximum degree : ", max_degree)#max degree
	# avg degree
	no_of_nodes = len(G.nodes())
	total_degree = sum(deg_list)
	print("Average degree : ", total_degree/no_of_nodes)#avg degree
	# clustering coefficient
	total_clustering_coeff = sum(nx.clustering(G).values())
	print("Average clustering coefficient : ", total_clustering_coeff/no_of_nodes)#avg clustering coeff
	# degree distrib 
	degree_distribution(G) # degree_distribution
	# avg path length and diameter
	try:
		print("Average path length : ", nx.average_shortest_path_length(G))
		print("Diameter : ", nx.diameter(G))
	except nx.NetworkXError:
		print("Graph is not connected. So computing average path length and diameter for its largest connected component ---")
		shortest_path_len = []
		diam = []
		for C in nx.connected_component_subgraphs(G):
			shortest_path_len.append(nx.average_shortest_path_length(C))
			diam.append(nx.diameter(C))
		print("Avg path length : ", max(shortest_path_len))
		print("Diameter : ", max(diam))

if __name__ == '__main__':
	try:
		G = nx.read_edgelist(sys.argv[1])
		analyse_graph(G)
	except FileNotFoundError:
		print("Check the file name you entered")