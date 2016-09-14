import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dmdocomo_app','dmdocomo_app')
G.edge['dmdocomo_app']['dmdocomo_app']['write-read'] = '[open open]'
G.add_edge('dmdocomo_app','dmdocomo_app')
G.edge['dmdocomo_app']['dmdocomo_app']['write-read'] = '[open open][write read]'
G.edge['dmdocomo_app']['dmdocomo_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()