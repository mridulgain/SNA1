import networkx as nx
import matplotlib.pyplot as plt
g = nx.read_edgelist('p2p-Gnutella08.txt')
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
fig.savefig("degree_distribution.png")
plt.show()