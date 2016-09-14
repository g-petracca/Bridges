import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('oneseg_mw','oneseg_mw')
G.edge['oneseg_mw']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('oneseg_mw','oneseg_mw')
G.edge['oneseg_mw']['oneseg_mw']['write-read'] = '[open open][setattr getattr]'
G.add_edge('oneseg_mw','oneseg_mw')
G.edge['oneseg_mw']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['oneseg_mw']['oneseg_mw']['fill'] = 'red'
G.add_edge('oneseg_mw','oneseg_mw')
G.edge['oneseg_mw']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()