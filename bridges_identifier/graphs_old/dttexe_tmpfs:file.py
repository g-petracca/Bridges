import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dttexe','dttexe')
G.edge['dttexe']['dttexe']['write-read'] = '[write read]'
G.edge['dttexe']['dttexe']['fill'] = 'red'
app = Viewer(G)
app.mainloop()