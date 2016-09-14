import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('container_service','container_service')
G.edge['container_service']['container_service']['write-read'] = '[write read]'
G.edge['container_service']['container_service']['fill'] = 'red'
app = Viewer(G)
app.mainloop()