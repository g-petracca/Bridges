import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('DMM-daemon','DMM-daemon')
G.edge['DMM-daemon']['DMM-daemon']['write-read'] = '[write read]'
G.edge['DMM-daemon']['DMM-daemon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()