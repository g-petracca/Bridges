import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('insthk','insthk')
G.edge['insthk']['insthk']['write-read'] = '[write read]'
G.edge['insthk']['insthk']['fill'] = 'red'
app = Viewer(G)
app.mainloop()