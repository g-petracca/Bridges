import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bootchecker','bootchecker')
G.edge['bootchecker']['bootchecker']['write-read'] = '[write read]'
G.edge['bootchecker']['bootchecker']['fill'] = 'red'
app = Viewer(G)
app.mainloop()