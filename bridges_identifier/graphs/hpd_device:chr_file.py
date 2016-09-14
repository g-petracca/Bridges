import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bintvoutservice','bintvoutservice')
G.edge['bintvoutservice']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bintvoutservice','surfaceflinger')
G.edge['bintvoutservice']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bintvoutservice','bintvoutservice')
G.edge['bintvoutservice']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bintvoutservice']['bintvoutservice']['fill'] = 'red'
G.add_edge('bintvoutservice','bintvoutservice')
G.edge['bintvoutservice']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bintvoutservice','surfaceflinger')
G.edge['bintvoutservice']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bintvoutservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('bintvoutservice','surfaceflinger')
G.edge['bintvoutservice']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['bintvoutservice']['fill'] = 'red'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()