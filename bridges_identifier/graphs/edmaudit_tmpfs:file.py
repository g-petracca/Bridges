import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('edmaudit','edmaudit')
G.edge['edmaudit']['edmaudit']['write-read'] = '[write read]'
G.edge['edmaudit']['edmaudit']['fill'] = 'red'
app = Viewer(G)
app.mainloop()