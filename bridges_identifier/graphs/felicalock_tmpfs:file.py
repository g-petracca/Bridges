import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('felicalock','felicalock')
G.edge['felicalock']['felicalock']['write-read'] = '[write read]'
G.edge['felicalock']['felicalock']['fill'] = 'red'
app = Viewer(G)
app.mainloop()