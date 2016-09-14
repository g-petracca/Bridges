import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('newAttr91','newAttr91')
G.edge['newAttr91']['newAttr91']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('newAttr91','newAttr91')
G.edge['newAttr91']['newAttr91']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('newAttr91','newAttr91')
G.edge['newAttr91']['newAttr91']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['newAttr91']['newAttr91']['fill'] = 'red'
G.add_edge('newAttr91','newAttr91')
G.edge['newAttr91']['newAttr91']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()