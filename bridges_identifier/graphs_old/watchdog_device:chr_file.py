import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('watchdogd','watchdogd')
G.edge['watchdogd']['watchdogd']['write-read'] = '[open open]'
G.add_edge('watchdogd','watchdogd')
G.edge['watchdogd']['watchdogd']['write-read'] = '[open open][write read]'
G.edge['watchdogd']['watchdogd']['fill'] = 'red'
G.add_edge('watchdogd','watchdogd')
G.edge['watchdogd']['watchdogd']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()