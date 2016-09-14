import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('per_mgr','per_mgr')
G.edge['per_mgr']['per_mgr']['write-read'] = '[write read]'
G.edge['per_mgr']['per_mgr']['fill'] = 'red'
app = Viewer(G)
app.mainloop()