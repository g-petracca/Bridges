import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lmkd']['lmkd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()