import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dtsconfigurator','dtsconfigurator')
G.edge['dtsconfigurator']['dtsconfigurator']['write-read'] = '[write read]'
G.edge['dtsconfigurator']['dtsconfigurator']['fill'] = 'red'
app = Viewer(G)
app.mainloop()