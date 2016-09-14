import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('nqs','nqs')
G.edge['nqs']['nqs']['write-read'] = '[write read]'
G.edge['nqs']['nqs']['fill'] = 'red'
app = Viewer(G)
app.mainloop()