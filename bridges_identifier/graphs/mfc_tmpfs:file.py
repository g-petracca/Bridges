import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mfc','mfc')
G.edge['mfc']['mfc']['write-read'] = '[write read]'
G.edge['mfc']['mfc']['fill'] = 'red'
app = Viewer(G)
app.mainloop()