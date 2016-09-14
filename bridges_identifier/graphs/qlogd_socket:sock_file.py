import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qlogd','appdomain')
G.edge['qlogd']['appdomain']['write-read'] = '[write read]'
G.edge['qlogd']['appdomain']['fill'] = 'red'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qlogd']['qlogd']['fill'] = 'red'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()