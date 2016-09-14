import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ipacm-diag','ipacm-diag')
G.edge['ipacm-diag']['ipacm-diag']['write-read'] = '[write read]'
G.edge['ipacm-diag']['ipacm-diag']['fill'] = 'red'
app = Viewer(G)
app.mainloop()