import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read]'
G.edge['rmt_storage']['rmt_storage']['fill'] = 'red'
app = Viewer(G)
app.mainloop()