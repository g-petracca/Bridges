import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
app = Viewer(G)
app.mainloop()