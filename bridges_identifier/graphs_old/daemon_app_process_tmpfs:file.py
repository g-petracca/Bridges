import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('daemon_app_process','daemon_app_process')
G.edge['daemon_app_process']['daemon_app_process']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['daemon_app_process']['daemon_app_process']['fill'] = 'red'
app = Viewer(G)
app.mainloop()