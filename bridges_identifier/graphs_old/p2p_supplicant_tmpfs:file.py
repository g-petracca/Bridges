import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('p2p_supplicant','p2p_supplicant')
G.edge['p2p_supplicant']['p2p_supplicant']['write-read'] = '[open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][write read][open open][setattr getattr][setattr getattr][write read][append read][write read][write read]'
G.edge['p2p_supplicant']['p2p_supplicant']['fill'] = 'red'
app = Viewer(G)
app.mainloop()