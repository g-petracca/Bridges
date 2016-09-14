import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qcomsysd','qcomsysd')
G.edge['qcomsysd']['qcomsysd']['write-read'] = '[open open][write read][open open][write read][write read]'
G.edge['qcomsysd']['qcomsysd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()