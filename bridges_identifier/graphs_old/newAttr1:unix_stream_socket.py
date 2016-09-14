import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['newAttr1']['newAttr1']['fill'] = 'red'
app = Viewer(G)
app.mainloop()