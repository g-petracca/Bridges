import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('vcsFPService','vcsFPService')
G.edge['vcsFPService']['vcsFPService']['write-read'] = '[write read]'
G.edge['vcsFPService']['vcsFPService']['fill'] = 'red'
app = Viewer(G)
app.mainloop()