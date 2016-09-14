import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('selinux_net','selinux_net')
G.edge['selinux_net']['selinux_net']['write-read'] = '[open open][write read]'
G.edge['selinux_net']['selinux_net']['fill'] = 'red'
app = Viewer(G)
app.mainloop()