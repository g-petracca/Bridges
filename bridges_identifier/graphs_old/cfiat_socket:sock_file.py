import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()