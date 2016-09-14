import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('init','keystore')
G.edge['init']['keystore']['write-read'] = '[setattr getattr]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['keystore']['keystore']['fill'] = 'red'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()