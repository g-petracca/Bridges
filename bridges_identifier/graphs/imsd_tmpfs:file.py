import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('imsd','imsd')
G.edge['imsd']['imsd']['write-read'] = '[write read]'
G.edge['imsd']['imsd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()