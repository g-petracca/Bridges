import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['seempd']['seempd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()