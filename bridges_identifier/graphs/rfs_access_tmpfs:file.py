import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['rfs_access']['rfs_access']['fill'] = 'red'
app = Viewer(G)
app.mainloop()