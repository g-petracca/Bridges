import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('empty_service','empty_service')
G.edge['empty_service']['empty_service']['write-read'] = '[write read]'
G.edge['empty_service']['empty_service']['fill'] = 'red'
app = Viewer(G)
app.mainloop()