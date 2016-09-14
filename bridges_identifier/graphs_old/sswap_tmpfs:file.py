import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('sswap','sswap')
G.edge['sswap']['sswap']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['sswap']['sswap']['fill'] = 'red'
app = Viewer(G)
app.mainloop()