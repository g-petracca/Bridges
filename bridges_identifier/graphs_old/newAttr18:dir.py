import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('newAttr86','newAttr86')
G.edge['newAttr86']['newAttr86']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('newAttr86','newAttr86')
G.edge['newAttr86']['newAttr86']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('newAttr86','newAttr86')
G.edge['newAttr86']['newAttr86']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['newAttr86']['newAttr86']['fill'] = 'red'
G.add_edge('newAttr86','newAttr86')
G.edge['newAttr86']['newAttr86']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('newAttr86','newAttr86')
G.edge['newAttr86']['newAttr86']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()