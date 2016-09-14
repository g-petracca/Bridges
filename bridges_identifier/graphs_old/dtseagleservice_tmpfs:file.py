import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dtseagleservice','dtseagleservice')
G.edge['dtseagleservice']['dtseagleservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['dtseagleservice']['dtseagleservice']['fill'] = 'red'
app = Viewer(G)
app.mainloop()