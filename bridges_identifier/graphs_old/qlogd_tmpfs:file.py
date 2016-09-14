import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['qlogd']['qlogd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()