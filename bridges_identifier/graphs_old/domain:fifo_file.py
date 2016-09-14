import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('unconfineddomain','unconfineddomain')
G.edge['unconfineddomain']['unconfineddomain']['write-read'] = '[open open]'
G.add_edge('unconfineddomain','unconfineddomain')
G.edge['unconfineddomain']['unconfineddomain']['write-read'] = '[open open][write read]'
G.edge['unconfineddomain']['unconfineddomain']['fill'] = 'red'
G.add_edge('unconfineddomain','unconfineddomain')
G.edge['unconfineddomain']['unconfineddomain']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()