import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('containerdomain','containerdomain')
G.edge['containerdomain']['containerdomain']['write-read'] = '[open open]'
G.add_edge('containerdomain','containerdomain')
G.edge['containerdomain']['containerdomain']['write-read'] = '[open open][write read]'
G.edge['containerdomain']['containerdomain']['fill'] = 'red'
G.add_edge('containerdomain','containerdomain')
G.edge['containerdomain']['containerdomain']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()