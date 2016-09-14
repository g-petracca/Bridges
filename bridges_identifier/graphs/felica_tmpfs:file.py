import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('felica','felica')
G.edge['felica']['felica']['write-read'] = '[write read]'
G.edge['felica']['felica']['fill'] = 'red'
app = Viewer(G)
app.mainloop()