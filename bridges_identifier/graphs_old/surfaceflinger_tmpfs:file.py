import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
app = Viewer(G)
app.mainloop()