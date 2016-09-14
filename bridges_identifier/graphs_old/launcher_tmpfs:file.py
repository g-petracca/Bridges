import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('launcher','launcher')
G.edge['launcher']['launcher']['write-read'] = '[write read]'
G.edge['launcher']['launcher']['fill'] = 'red'
app = Viewer(G)
app.mainloop()