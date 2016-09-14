import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('racoon','racoon')
G.edge['racoon']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['racoon']['racoon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()