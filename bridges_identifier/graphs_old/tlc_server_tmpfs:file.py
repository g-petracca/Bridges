import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('tlc_server','tlc_server')
G.edge['tlc_server']['tlc_server']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read]'
G.edge['tlc_server']['tlc_server']['fill'] = 'red'
app = Viewer(G)
app.mainloop()