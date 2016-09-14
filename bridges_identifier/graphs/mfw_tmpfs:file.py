import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mfw','mfw')
G.edge['mfw']['mfw']['write-read'] = '[write read]'
G.edge['mfw']['mfw']['fill'] = 'red'
app = Viewer(G)
app.mainloop()