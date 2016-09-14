import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('wfd_app','wfd_app')
G.edge['wfd_app']['wfd_app']['write-read'] = '[open open][write read][append read][write read][setopt getopt][write read]'
G.edge['wfd_app']['wfd_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()