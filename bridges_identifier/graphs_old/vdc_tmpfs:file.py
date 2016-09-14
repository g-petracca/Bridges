import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('vdc','vdc')
G.edge['vdc']['vdc']['write-read'] = '[write read][write read]'
G.edge['vdc']['vdc']['fill'] = 'red'
app = Viewer(G)
app.mainloop()