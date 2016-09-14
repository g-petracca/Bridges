import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('audiod','audiod')
G.edge['audiod']['audiod']['write-read'] = '[open open][write read][append read][write read]'
G.edge['audiod']['audiod']['fill'] = 'red'
app = Viewer(G)
app.mainloop()