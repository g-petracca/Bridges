import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('policyloader_app','policyloader_app')
G.edge['policyloader_app']['policyloader_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('policyloader_app','policyloader_app')
G.edge['policyloader_app']['policyloader_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('policyloader_app','policyloader_app')
G.edge['policyloader_app']['policyloader_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['policyloader_app']['policyloader_app']['fill'] = 'red'
G.add_edge('policyloader_app','policyloader_app')
G.edge['policyloader_app']['policyloader_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()