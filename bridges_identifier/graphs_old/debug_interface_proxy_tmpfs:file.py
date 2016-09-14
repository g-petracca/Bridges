import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['debug_interface_proxy']['debug_interface_proxy']['fill'] = 'red'
app = Viewer(G)
app.mainloop()