import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('isolated_app','isolated_app')
G.edge['isolated_app']['isolated_app']['write-read'] = '[open open][setattr getattr][write read][write read][write read]'
G.edge['isolated_app']['isolated_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()