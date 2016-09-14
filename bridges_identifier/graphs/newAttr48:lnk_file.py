import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_domain']['system_domain']['fill'] = 'red'
G.add_edge('system_domain','system_domain')
G.edge['system_domain']['system_domain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()