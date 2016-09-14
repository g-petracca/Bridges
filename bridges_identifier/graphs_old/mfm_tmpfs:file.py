import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mfm','mfm')
G.edge['mfm']['mfm']['write-read'] = '[write read]'
G.edge['mfm']['mfm']['fill'] = 'red'
app = Viewer(G)
app.mainloop()