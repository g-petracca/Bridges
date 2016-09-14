import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','newAttr86')
G.edge['adbd']['newAttr86']['write-read'] = '[setattr getattr]'
G.add_edge('appdomain','newAttr86')
G.edge['appdomain']['newAttr86']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr86','newAttr86')
G.edge['newAttr86']['newAttr86']['write-read'] = '[open open]'
G.add_edge('newAttr86','newAttr86')
G.edge['newAttr86']['newAttr86']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr86','newAttr86')
G.edge['newAttr86']['newAttr86']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr86']['newAttr86']['fill'] = 'red'
G.add_edge('newAttr86','newAttr86')
G.edge['newAttr86']['newAttr86']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','newAttr86')
G.edge['untrusteddomain']['newAttr86']['write-read'] = '[setattr getattr]'
G.add_edge('untrusteddomain','newAttr86')
G.edge['untrusteddomain']['newAttr86']['write-read'] = '[setattr getattr][setattr getattr]'
app = Viewer(G)
app.mainloop()