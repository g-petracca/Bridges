import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adsprpcd','adsprpcd')
G.edge['adsprpcd']['adsprpcd']['write-read'] = '[write read]'
G.edge['adsprpcd']['adsprpcd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()