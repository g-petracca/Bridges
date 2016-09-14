import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('servicemanager','servicemanager')
G.edge['servicemanager']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['servicemanager']['servicemanager']['fill'] = 'red'
app = Viewer(G)
app.mainloop()