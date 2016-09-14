import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['init']['init']['fill'] = 'red'
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()