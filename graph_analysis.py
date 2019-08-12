import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.special import zetac
from scipy.optimize import curve_fit

def fit_func(x,a):
	 return (x**-a)/zetac(a)

def degree_distribution(g):
	dd = {}
	for n in g.nodes():
		deg = g.degree(n)
		if deg  not in dd:
			dd[deg] = 0
		dd[deg] += 1
	deg_count = sorted(dd.items ())
	k = [deg for (deg,count) in deg_count]
	no_of_nodes = len(g.nodes())
	pk = [count/no_of_nodes for (deg, count) in deg_count]
	popt, pcov = curve_fit(fit_func, k, pk)
	perr = np.sqrt(np.diag(pcov))
	print("Power law exponent : %5.5f (with standard deviation error : %5.5f)" %(popt, perr))
	# visualisation
	plt.plot(k, pk, 'b-', label='data')
	plt.plot(k, fit_func(k, *popt), 'r-', label='fit: alpha = %5.3f \nstandard deviation errr = %5.5f' %(popt, perr))
	plt.xlabel('k')
	plt.ylabel('p(k)')
	title = "Degree  Distribution" + " for <%s>" % (sys.argv[1].split('.')[0])
	plt.title(title)
	plt.legend()
	plt.savefig(title + ".png")
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
	print("Average degree : %5.5f" %(total_degree/no_of_nodes))#avg degree
	# clustering coefficient
	total_clustering_coeff = sum(nx.clustering(G).values())
	print("Average clustering coefficient : %5.5f" %(total_clustering_coeff/no_of_nodes))#avg clustering coeff
	# degree distrib 
	degree_distribution(G) # degree_distribution
	# avg path length and diameter
	try:
		print("Average path length : %5.5f" %(nx.average_shortest_path_length(G)) )
		print("Diameter : ", nx.diameter(G))
	except nx.NetworkXError:
		print("Graph is not connected. So computing average path length and diameter for its largest connected component ---")
		shortest_path_len = []
		diam = []
		for C in nx.connected_component_subgraphs(G):
			shortest_path_len.append(nx.average_shortest_path_length(C))
			diam.append(nx.diameter(C))
		print("Avg path length : %5.5f" %(max(shortest_path_len)) )
		print("Diameter : ", max(diam))

if __name__ == '__main__':
	try:
		G = nx.read_edgelist(sys.argv[1])
		analyse_graph(G)
	except FileNotFoundError:
		print("Check the file name you have entered")
	except IndexError:
		print("Enter input file name as command line argument")
		print("Usage : python graph_analysis.py file_name")
	except TypeError:
		print("You should enter your graph in EDGE LIST format")
