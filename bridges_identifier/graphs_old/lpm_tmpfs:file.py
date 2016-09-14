import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lpm']['lpm']['fill'] = 'red'
app = Viewer(G)
app.mainloop()