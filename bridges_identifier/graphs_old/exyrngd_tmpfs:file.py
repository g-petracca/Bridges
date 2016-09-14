import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('exyrngd','exyrngd')
G.edge['exyrngd']['exyrngd']['write-read'] = '[write read]'
G.edge['exyrngd']['exyrngd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()