import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()