import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('port-bridge','port-bridge')
G.edge['port-bridge']['port-bridge']['write-read'] = '[write read][open open]'
G.add_edge('port-bridge','port-bridge')
G.edge['port-bridge']['port-bridge']['write-read'] = '[write read][open open][write read]'
G.edge['port-bridge']['port-bridge']['fill'] = 'red'
G.add_edge('port-bridge','port-bridge')
G.edge['port-bridge']['port-bridge']['write-read'] = '[write read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()