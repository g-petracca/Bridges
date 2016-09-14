import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('logd','logd')
G.edge['logd']['logd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['logd']['logd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()