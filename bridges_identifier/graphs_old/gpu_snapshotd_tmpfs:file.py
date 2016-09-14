import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('gpu_snapshotd','gpu_snapshotd')
G.edge['gpu_snapshotd']['gpu_snapshotd']['write-read'] = '[write read]'
G.edge['gpu_snapshotd']['gpu_snapshotd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()