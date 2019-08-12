import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import zetac

def fit_func(x,a):
	 return (x**-a)/zetac(a)

g = nx.read_edgelist('el-p2p-Gnutella08.txt')
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
#ploting
plt.plot(k, pk, 'b-', label='data')
plt.plot(k, fit_func(k, *popt), 'r-',
         label='fit: alpha = %5.3f \nstandard deviation errr = %5.5f' %(popt, perr))
plt.xlabel('k')
plt.ylabel('p(k)')
plt.title("Degree  Distribution"+" for <Network>")
plt.legend()
plt.show()
