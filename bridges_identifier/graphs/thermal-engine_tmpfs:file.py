import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read]'
G.edge['thermal-engine']['thermal-engine']['fill'] = 'red'
app = Viewer(G)
app.mainloop()