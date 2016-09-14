import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('container_app','container_app')
G.edge['container_app']['container_app']['write-read'] = '[write read]'
G.edge['container_app']['container_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()