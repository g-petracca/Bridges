import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qosmgr','qosmgr')
G.edge['qosmgr']['qosmgr']['write-read'] = '[write read]'
G.edge['qosmgr']['qosmgr']['fill'] = 'red'
app = Viewer(G)
app.mainloop()