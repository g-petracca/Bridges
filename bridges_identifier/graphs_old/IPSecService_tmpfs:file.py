import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('IPSecService','IPSecService')
G.edge['IPSecService']['IPSecService']['write-read'] = '[write read]'
G.edge['IPSecService']['IPSecService']['fill'] = 'red'
app = Viewer(G)
app.mainloop()