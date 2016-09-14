import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('atfwd','atfwd')
G.edge['atfwd']['atfwd']['write-read'] = '[write read]'
G.edge['atfwd']['atfwd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()