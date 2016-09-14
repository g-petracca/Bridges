import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read]'
G.edge['perfd']['perfd']['fill'] = 'red'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()