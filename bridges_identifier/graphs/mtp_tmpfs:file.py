import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mtp','mtp')
G.edge['mtp']['mtp']['write-read'] = '[write read][write read]'
G.edge['mtp']['mtp']['fill'] = 'red'
app = Viewer(G)
app.mainloop()