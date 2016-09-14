import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('wiperiface','wiperiface')
G.edge['wiperiface']['wiperiface']['write-read'] = '[write read]'
G.edge['wiperiface']['wiperiface']['fill'] = 'red'
app = Viewer(G)
app.mainloop()