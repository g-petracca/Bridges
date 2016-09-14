import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open]'
G.add_edge('kernel','sswap')
G.edge['kernel']['sswap']['write-read'] = '[open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kernel']['kernel']['fill'] = 'red'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('kernel','sswap')
G.edge['kernel']['sswap']['write-read'] = '[open open][write read]'
G.edge['kernel']['sswap']['fill'] = 'red'
G.add_edge('kernel','sswap')
G.edge['kernel']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('sswap','kernel')
G.edge['sswap']['kernel']['write-read'] = '[open open]'
G.add_edge('sswap','sswap')
G.edge['sswap']['sswap']['write-read'] = '[open open]'
G.add_edge('sswap','kernel')
G.edge['sswap']['kernel']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sswap','kernel')
G.edge['sswap']['kernel']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sswap']['kernel']['fill'] = 'red'
G.add_edge('sswap','kernel')
G.edge['sswap']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sswap','sswap')
G.edge['sswap']['sswap']['write-read'] = '[open open][write read]'
G.edge['sswap']['sswap']['fill'] = 'red'
G.add_edge('sswap','sswap')
G.edge['sswap']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open]'
G.add_edge('vold','sswap')
G.edge['vold']['sswap']['write-read'] = '[open open]'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['kernel']['fill'] = 'red'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','sswap')
G.edge['vold']['sswap']['write-read'] = '[open open][write read]'
G.edge['vold']['sswap']['fill'] = 'red'
G.add_edge('vold','sswap')
G.edge['vold']['sswap']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()