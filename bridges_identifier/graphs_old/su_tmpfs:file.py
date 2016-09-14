import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('su','su')
G.edge['su']['su']['write-read'] = '[write read]'
G.edge['su']['su']['fill'] = 'red'
app = Viewer(G)
app.mainloop()