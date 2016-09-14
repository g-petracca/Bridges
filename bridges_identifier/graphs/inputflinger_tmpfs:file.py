import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('inputflinger','inputflinger')
G.edge['inputflinger']['inputflinger']['write-read'] = '[write read]'
G.edge['inputflinger']['inputflinger']['fill'] = 'red'
app = Viewer(G)
app.mainloop()