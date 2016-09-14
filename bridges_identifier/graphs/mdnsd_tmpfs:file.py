import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mdnsd','mdnsd')
G.edge['mdnsd']['mdnsd']['write-read'] = '[write read]'
G.edge['mdnsd']['mdnsd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()