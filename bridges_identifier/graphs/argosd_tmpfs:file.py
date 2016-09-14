import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('argosd','argosd')
G.edge['argosd']['argosd']['write-read'] = '[write read]'
G.edge['argosd']['argosd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()