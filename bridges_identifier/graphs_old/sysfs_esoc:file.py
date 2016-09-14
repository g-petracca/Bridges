import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read]'
G.edge['domain']['rild']['fill'] = 'red'
G.add_edge('time_daemon','rild')
G.edge['time_daemon']['rild']['write-read'] = '[write read]'
G.edge['time_daemon']['rild']['fill'] = 'red'
app = Viewer(G)
app.mainloop()