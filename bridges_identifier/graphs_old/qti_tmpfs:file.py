import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['qti']['qti']['fill'] = 'red'
app = Viewer(G)
app.mainloop()