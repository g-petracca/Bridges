import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('scs','scs')
G.edge['scs']['scs']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['scs']['scs']['fill'] = 'red'
app = Viewer(G)
app.mainloop()