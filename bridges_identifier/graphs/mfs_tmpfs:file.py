import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mfs','mfs')
G.edge['mfs']['mfs']['write-read'] = '[write read]'
G.edge['mfs']['mfs']['fill'] = 'red'
app = Viewer(G)
app.mainloop()