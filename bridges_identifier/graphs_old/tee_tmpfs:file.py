import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read]'
G.edge['tee']['tee']['fill'] = 'red'
app = Viewer(G)
app.mainloop()