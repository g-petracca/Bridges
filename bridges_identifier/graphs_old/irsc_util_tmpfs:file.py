import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('irsc_util','irsc_util')
G.edge['irsc_util']['irsc_util']['write-read'] = '[write read]'
G.edge['irsc_util']['irsc_util']['fill'] = 'red'
app = Viewer(G)
app.mainloop()