import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['drmserver']['drmserver']['fill'] = 'red'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['drmserver']['mediaserver']['fill'] = 'red'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()